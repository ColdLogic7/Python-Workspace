# 🔍 SQLi Login Form Scanner

A lightweight Python CLI tool that checks login forms for potential SQL injection vulnerabilities using error-based, boolean-based, and time-based detection methods.

This project focuses on authorized security testing and detection only — it does not perform exploitation or data extraction.

## ✨ Features

- 🔎 Identify login forms using BeautifulSoup
- 🧪 Test error-based SQL injection payloads
- ⚖️ Compare responses for boolean-based detection
- ⏱️ Check response delays for time-based detection
- 🔐 Extract and reuse CSRF tokens when available
- 📦 Load configurable payloads from JSON
- ⚠️ Handle request failures and stop when a finding is detected

## 🛠 Skills Practiced

- HTTP requests using `requests`
- Persistent sessions and custom headers
- HTML parsing with `BeautifulSoup`
- JSON file handling
- Command-line arguments with `argparse`
- Baseline response comparison
- Defensive programming and exception handling
- Sequential testing and early returns

## 🚀 How To Run

Install dependencies:

```bash
pip install requests beautifulsoup4 lxml
```

Run the scanner:

```bash
python SQL_scanner.py --url https://example.com/login
```

Optional arguments:

```bash
--username-field username
--password-field password
--timeout 5
--time-delay 5
```

Keep `payloads.json` in the same directory as the Python script.

**Important:** Only scan systems you own or have explicit permission to test. Unauthorized security testing may be illegal.

## 📂 Project Structure

```text
SQLi-Scanner/
├── SQL_scanner.py
├── payloads.json
└── README.md
```

## 📚 What I Learned

- A detection method must identify an expected response pattern, not just any response change.
- Baseline comparison provides a reference for boolean-based checks.
- Defensive `None` checks prevent failures when requests return no response.
- `requests.Session()` maintains consistent headers across requests.
- Sequential triage with early returns avoids unnecessary tests.
- Security detection involves balancing false positives and false negatives.

## ⚠️ Known Limitations (v1)

- **Union-based detection removed:** The response-length comparison approach produced too many false positives on pages with dynamic content. A reliable implementation requires column-count enumeration, planned for a future version.
- Only login-form input fields are tested.
- JavaScript-driven forms are not supported by `requests`.
- Detection results are indicators, not proof that a system is secure or vulnerable.
- Time-based results can be inconclusive due to network delays.

## 💡 Biggest Takeaway

> **A smaller, honest security tool is better than a feature-rich tool that reports unreliable results.**

Cutting an unreliable detection method is not failure. Knowing what your tool cannot reliably detect—and documenting that limitation—is an important part of security engineering.

## 🔮 Future Improvements

- Implement reliable union-based detection.
- Improve baseline comparison for dynamic pages.
- Add support for additional form fields.
- Improve detection confidence and reporting.
- Add automated tests using controlled vulnerable applications.

## 👨‍💻 Author

**ColdLogic7**

Learning Python through practical projects, security experimentation, and documenting lessons learned.