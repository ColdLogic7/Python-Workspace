# 🐙 GitHub Profile Analyzer

A Python CLI tool that analyzes GitHub profiles using the GitHub REST API, displaying profile information, social metrics, repository details, and programming language statistics.

## ✨ Features

* 🔰 Display basic profile information
* 🎭 Show followers, following, and public repositories
* 🗂️ List repositories, stars, forks, and languages
* 🔥 Display top 3 programming languages with visual bars
* 📄 Fetch repositories across multiple pages
* ⚠️ Handle API errors and monitor rate limits

## 🛠 Skills Practiced

* GitHub REST API and Bearer token authentication
* `requests` and HTTP response handling
* Pagination using `while` and `extend()`
* `collections.Counter` and `.most_common()`
* Dictionaries, list processing, and ternary expressions
* API error handling and response headers

## 🚀 How To Run

```bash
pip install requests
python GitHub_profile_analyzer.py
```

Add your GitHub personal access token to `API_KEY` before running.

**Security note:** Never publish your real token on GitHub. Use an environment variable to keep it private.

## 📂 Project Structure

```text
GitHub-Profile-Analyzer/
├── GitHub_profile_analyzer.py
└── README.md
```

## 📚 What I Learned — Project 12

* Authenticate API requests using `Authorization: Bearer TOKEN`.
* Fetch paginated data and combine results with `extend()`.
* Check HTTP errors using `raise_for_status()` before parsing JSON.
* Count language usage with `Counter(languages).most_common(3)`.
* Read rate-limit information from response headers.
* Handle missing API values with `.get()` and fallback values.

## ⚠️ Lessons Worth Remembering

* Check for `None` before accessing data from an external source.
* Always check the response status before parsing JSON.
* Collect data before processing and displaying statistics.
* Use `item` to access the current dictionary and `idx` for numbering.
* Convert calculated values to integers before using them for string multiplication.

## 💡 Biggest Takeaway

> **Follow the correct data flow: fetch, validate, collect, process, and display.**

## 🔮 Future Improvements

* Move the API token into an environment variable.
* Add repository filtering and sorting.
* Export analysis results to JSON or CSV.
* Improve language statistics and visualizations.

## 📈 Roadmap Progress

**12 / 26 projects completed** ✅

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.
