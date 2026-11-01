import requests
import json
from bs4 import BeautifulSoup
import time
import argparse

THRESHOLD = 20 # used to detect minor, natural flunctuations in web page response


def load_payloads():
    try:
        with open('payloads.json','r',encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("❌ Error: 'payloads.json' Not Found!")
        return None

def is_login_page(url, timeout):
    try:
        response = requests.get(url=url,timeout=timeout)
    except requests.exceptions.RequestException as err:
        print(f"❌ Error: Something went wrong: {err}")
        return False
    
    soup = BeautifulSoup(response.text,"lxml")
    if soup.find('form') is not None or soup.find('input', type='password'):
        return True
    return False

def get_csrf_token(session, url, timeout):
    response = session.get(url, timeout=timeout)
    soup = BeautifulSoup(response.text, "lxml")
    token_input = soup.find('input', {'name': 'csrf'})
    if token_input:
        return token_input.get('value')
    return None

def send_payload(url, field_name, payload,other_field_name, other_field_value, timeout):
    if not url.startswith('http') and not url.startswith('https'):
        url = 'https://' + url
    session = requests.sessions.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    csrf_token = get_csrf_token(session, url, timeout)
    data = {
        field_name: payload,
        other_field_name: other_field_value
    }
    if csrf_token:
        data['csrf'] = csrf_token
    try:
        response = session.post(url=url, data=data, timeout=timeout)
        return response
    except requests.exceptions.ConnectionError:
        print("[⚠️ Could not reach target — check URL and internet connection!]")
    except requests.exceptions.Timeout:
        print("[⚠️  Timeout on time-based check — result inconclusive!]")
    except Exception as e:
        print(f"DEBUG: caught exception type={type(e).__name__}, msg={e}")
    return None
    
    

def get_baseline(url, username_field, password_field, timeout):
    return send_payload(
        url=url,
        field_name=username_field,
        payload='definitely_not_a_user_xq9z', 
        other_field_name=password_field, 
        other_field_value='wrongpassword123', 
        timeout=timeout
        )
  

def check_error_based(response, error_keywords):
    if not response:
        return None
    response_text = response.text.lower()
    for err in error_keywords:
        if err.lower() in response_text:
            return err
    return None

def check_boolean_based(true_resp, false_resp, baseline):
    if not true_resp or not false_resp or not baseline:
        return False
    is_true_matching = abs(len(true_resp.text) - len(baseline.text)) <= THRESHOLD
    is_false_matching = abs(len(false_resp.text) - len(baseline.text)) > THRESHOLD
    return is_true_matching and is_false_matching

def check_time_based(url, field_name, payload, other_field_name, other_field_value, expected_delay, timeout):
    if not url.startswith('http') and not url.startswith('https'):
        url = 'http://' + url
    data = {
        field_name: payload,
        other_field_name: other_field_value
    }
    actual_timeout = max(timeout, expected_delay + 3)

    try:
        start_time = time.time()
        response = requests.post(url=url, data=data, timeout=actual_timeout)
        elapsed_time = time.time() - start_time

        if elapsed_time >= (expected_delay * 0.9):
            return True
    except requests.exceptions.Timeout:
        return True 
    except requests.exceptions.RequestException as err:
        pass
    return False

def display_result(finding):
    if finding:
        print("\u2500" * 38)
        print("✅ VULNERABLE — SQL Injection Detected")
        print("\u2500" * 38)
        print(f"Type: {finding.get('type')}")
        print(f"Payload: {finding.get('payload')}")
        print(f"Field: {finding.get('field')}")
        print(f"Evidence: {finding.get('evidence')}")
        print("\u2500" * 38)

def run_scan(url, username_field, passowrd_filed, payload_data, args):
    timeout = args.timeout
    time_delay = args.time_delay
    metadata = payload_data.get('metadata', {})
    error_keywords = metadata.get('db_error_keywords', [])

    print(f"🔍 Target: {url}")
    print(f"📋 Fields: {username_field} | {passowrd_filed}")
    print('\u2500' * 38)

    baseline = get_baseline(url, username_field, passowrd_filed, timeout)
    if not baseline:
        print("❌ Could not establish baseline response. Exiting scan.")
        return

    total_tested = 0

    # Error-based
    print(f"[1/3] Testing Error-based payloads...  {len(payload_data['error_based']['payloads'])}  payloads")
    for payload in payload_data['error_based']['payloads']:
        total_tested += 1
        resp = send_payload(url, username_field, payload, passowrd_filed, 'wrongpass', timeout)
        err_match = check_error_based(resp, error_keywords)
        if err_match:
            display_result({
                'type': 'Error-based',
                'payload': payload,
                'field': username_field,
                'evidence': f"Response contained {err_match}"
            })
            return

    # Union-based
    # Removed Uninon-based injection because it produce false-positive result

    # Boolean-based
    print(f"[2/3] Testing Boolean-based payloads... {len(payload_data['boolean_based']['true_payloads'])*2} payloads")
    true_payloads = payload_data['boolean_based']['true_payloads']
    false_payloads = payload_data['boolean_based']['false_payloads']
    for t_payload, f_payload in zip(true_payloads, false_payloads):
        total_tested += 2
        true_resp = send_payload(url, username_field, t_payload, passowrd_filed, 'wrongpass', timeout)
        false_resp = send_payload(url, username_field, f_payload, passowrd_filed, 'wrongpass', timeout)
        if check_boolean_based(true_resp, false_resp, baseline):
            display_result({
                'type': 'Boolean-based',
                'payload': f"True {t_payload} / False: {f_payload}",
                'field': username_field,
                'evidence': "True response matches baseline, false response differs"
            })
            return

    # Time-based
    print(f"[3/3] Testing Time-based payloads... {len(payload_data['time_based']['payloads'])} payloads")
    for payload in payload_data['time_based']['payloads']:
        total_tested += 1
        is_delayed = check_time_based(url, username_field, payload, passowrd_filed, 'wrongpass',time_delay, timeout)
        if is_delayed:
            display_result({
                'type': 'Time-based',
                'payload': payload,
                'field': username_field,
                'evidence': f'Response took >= {time_delay * 0.9} seconds'
            })
            return
        
    # clean result screen
    print("\u2500" * 38)
    print("✅ No SQL injection detected")
    print(f"Tested {total_tested} payloads across 3 methods")
    print("\u2500" * 38)


def main():
    parser = argparse.ArgumentParser(
    description='🔍 SQLi Scanner — Detect SQL injection in login forms',
    epilog='Checks: error-based, boolean-based, time-based'
    )
    parser.add_argument('-u', '--url', type=str, required=True,
                    help='Login page URL e.g https://example.com/login')
    parser.add_argument('--username-field', type=str, default='username',
                    help='Name of username input field (default: username)')
    parser.add_argument('--password-field', type=str, default='password',
                    help='Name of password input field (default: password)')
    parser.add_argument('--timeout', type=int, default=5,
                    help='Request timeout in seconds (default: 5)')
    parser.add_argument('--time-delay', type=int, default=5,
                    help='Expected delay for time-based checks (default: 5)')
    args = parser.parse_args()

    payload_data = load_payloads()
    if not payload_data:
        return

    url = args.url
    if not url.startswith('http') and not url.startswith('https'):
        url = 'https://' + url

    print(f"[*] Checking if target is a valid login page...")
    if not is_login_page(args.url, args.timeout):
        print("❌ URL does not appear to be a login page (no form or password field found)")
        return

    run_scan(url, args.username_field, args.password_field, payload_data, args)


if __name__ == '__main__':
    main()