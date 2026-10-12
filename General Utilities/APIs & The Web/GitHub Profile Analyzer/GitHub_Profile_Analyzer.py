import requests
from collections import Counter


API_KEY = 'Your_GitHub_Token_Here' # Insert your gitHub token here 
SEPARATOR = '-'*50
SMALL_SEP = '-'*7

if not API_KEY or API_KEY == 'Your_GitHub_Token_Here':
    raise ValueError("❌ Error: Please add your Valid GitHub token before running.")

def make_request(username, return_type, params=None) -> dict | None:
    profile_url = f'https://api.github.com/users/{username}'
    repo_url = f'https://api.github.com/users/{username}/repos'

    header = {
        'Authorization': f'Bearer {API_KEY}',
        "Accept": "application/vnd.github+json"
    }
    try:
        if return_type == 'user oriented':
            response = requests.get(url=profile_url, headers=header, timeout=5)
        else:
            response = requests.get(url=repo_url, params=params, headers=header, timeout=5)
        remaining = response.headers.get('X-RateLimit-Remaining')
        response.raise_for_status()
        data = response.json() 
        if isinstance(data, list) and len(data) == 0:
            print("\n\t[⚠️  No More Pages / Repositories]")
        if int(remaining) <= 10:
            print("\n\t[⚠️  Warning: Rate Limiting is Less Than 10.]")
        return data
    except requests.exceptions.ConnectionError:
        print("\n\t[⚠️  No Internet Connection!]")
    except requests.exceptions.Timeout:
        print("\n\t[⚠️  Request Timed Out!]")
    except requests.exceptions.HTTPError as err:
        print(f"\n\t[❌ Captured Error: GitHub user '{username}' was not found.]") if err.response.status_code == 404 else print(f"\n\t[❌ HTTP Error: {err}]") 
    except requests.exceptions.RequestException as err:
        print(f"\n\t[❌ An unexpected error occurred: {err}]")
    return None

def access_repo(username):
    all_repos = []
    page = 1
    while True:
        params = {
            'per_page': 100,
            'page': page
        }
        data = make_request(username=username, return_type='repo oriented',params=params)
        if not data:
            break
        all_repos.extend(data)
        page += 1
    return all_repos

def display_menu():
    print(f"\n\t{SMALL_SEP} ⚙️  MENU {SMALL_SEP}")
    print("1. 🔰 Basic Information")
    print("2. 🎭 Social Matrics")
    print("3. 🗂️  Repositories & Code Metadata")
    print("4. 🔥 Language Statistics")
    print("5. [← Exit")

    print(SEPARATOR)
    while True:
        try:
            desired_option = int(input("\t👉 Choose a Option [1-5]: ").strip())
            if 1 <= desired_option <= 5:
                return desired_option
            else:
                print("\n\t[❌ Error: Choose a number between 1-5!]")
        except ValueError:
            print("\n\t[❌ Error: Please Choose a Valid Number!]")

def basic_info(username):
    data = make_request(username=username, return_type='user oriented')
    if data is None or not data:
        print("\n\t[❌ Error: Something went wrong...]")
        return
    bio = data.get('bio') if data.get('bio') else 'Unavailable bio'
    bio_display = bio if len(bio) < 70 else bio[:70] + '...'
    created_at = data.get('created_at')
    name = data.get('name')
    print(f"\n{SMALL_SEP} 🔰 Basic Information {SMALL_SEP}")
    print(f"🙍 Name:    {name if name else username}")
    print(f"📝 Biography: {bio_display}")
    print(f"🔗 Link:    {data.get('html_url')}")
    print(f"💼 Company:  {data.get('company')}")
    print(f"🪄  Created: {created_at[:10]}")
    print(f"🗺️  Location: {data.get('location')}")
    print(SEPARATOR)

def social_metrics(username):
    data = make_request(username=username, return_type='user oriented')
    if data is None or not data:
        print("\n\t[❌ Error: Something went wrong...]")
        return
    print(f"\n{SMALL_SEP} 🎭 Social Metrics {SMALL_SEP}")
    print(f"❄️  Following: {data.get('following', 0)}")
    print(f"💪 Follower: {data.get('followers', 0)}")
    print(f"🍁 Total Projects: {data.get('public_repos', 0)}")
    print(f"🏙️  Collaborators: {data.get('collaborators', 0)}")
    twitter = data.get('twitter_username')
    twitter_display = f"@{twitter}" if twitter else 'Not Linked'
    print(f"💎 Twitter a/c: {twitter_display}")
    print(SEPARATOR)

def repos_meta(username):
    data = access_repo(username=username)
    if data is None or not data:
        print("\n\t[❌ Error: Something went wrong...]")
        return
    owner_login = data[0]['owner']['login'] if isinstance(data, list) else username
    print(f"\n{SMALL_SEP} 🗂️  Repositories & Code Metadata of {owner_login} {SMALL_SEP}")
    header = f"{'#':<3}|{'Repo Name':<18}|{'Stars':<5}|{'Forks':<5}|{'Language':<10}|{'Link'}"
    print(header)
    print(f"{'-'*len(header)}")
    for idx, item in enumerate(data):
        raw_name = item.get('name', 'Unknown')
        repo_name = raw_name if len(raw_name) <= 18 else raw_name[:15] + '...'
        raw_lang = item.get('language') or 'None'
        lang_name = raw_lang if len(raw_lang) <= 8 else raw_lang[:5] + '...'
        stars = item.get('stargazers_count', 0)
        forks = item.get('forks', 0)
        url = item.get('html_url', '')
        print(f"{idx+1:<3}|{repo_name:<18}|{stars:<5}|{forks:<5}|{lang_name:<10}|{url}")
    print(SEPARATOR)

def lang_stat(username):
    data = access_repo(username=username)
    if data is None or not data:
        print("\n\t[❌ Error: Something went wrong...]")
        return
    owner_name = data[0]['owner']['login'] if isinstance(data, list) else username
    print(f"\n{SMALL_SEP} 🔥 TOP 3 Language Used by {owner_name} {SMALL_SEP}")
    languages = []
    for item in data:
        lang = item.get('language')
        if lang:
            languages.append(lang)

    if not languages:
        print("\n\t [🥹 No Language metrics available for this user.]")
        print(SEPARATOR)
        return
    
    count_analyzer = Counter(languages)
    top_3_langs = count_analyzer.most_common(3)
    
    total_count = sum(count for _, count in top_3_langs)

    for lang_name, count_item in top_3_langs:
        percentage = (count_item/total_count) * 100
        bar_length = int(percentage / 10)
        bar_visual = '█' * bar_length if bar_length > 0 else '░'
        print(f"[+] {lang_name:<10}: [{bar_visual:<10}] {percentage:.1f}% ({count_item} repos) ")
    print(SEPARATOR)

def main():
    print(f"{SMALL_SEP} 🤖 GitHub Profile Analyzer {SMALL_SEP}")
    print()
    get_username = input("🌿 Enter GitHub Username to Analyze it: ").strip()

    while True:
        get_operation = display_menu()
        if get_operation == 1:
            basic_info(get_username)
        elif get_operation == 2:
            social_metrics(get_username)
        elif get_operation == 3:
            repos_meta(get_username)
        elif get_operation == 4:
            lang_stat(get_username)
        else:
            print("\n\t 👋 Good Bye!")
            exit(0)
        
if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\n\t [💥 Interrupted by User!]")
            exit(0)