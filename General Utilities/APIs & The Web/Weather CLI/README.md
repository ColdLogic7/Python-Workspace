# 🌦️ Weather CLI

A command-line weather application built with Python that uses the OpenWeatherMap API to fetch current weather and 5-day forecasts.

## ✨ Features

* 🌍 Current weather by city
* 📍 Current weather by ZIP code
* 📅 5-day forecast
* 🌡️ Celsius / Fahrenheit selection
* ⚠️ Handles API, network, timeout, and invalid request errors
* 🔄 Option to make multiple requests in one session

## 🛠 Skills Practiced

* Working with APIs using `requests`
* Query parameters and JSON responses
* HTTP error handling
* Exception hierarchy
* Functions and code reuse
* Filtering API response data
* CLI input validation

## 🚀 How To Run

```bash
pip install requests
python Weather_CLI.py
```

Add your own OpenWeatherMap API key before running the program.

## 📂 Project Structure

```text
Weather-CLI/
├── Weather_CLI.py
└── README.md
```

## 📚 What I Learned — Project 11

* `requests.get()` with parameter dictionaries
* `response.raise_for_status()`
* `response.json()`
* Handling `ConnectionError`, `Timeout`, `HTTPError`, and `RequestException`
* Filtering forecast data by time
* Reusing one request function for different API operations

## ⚠️ Lessons Worth Remembering

* External systems can fail, so API calls need proper error handling.
* General exceptions should come after specific exceptions.
* Avoid hardcoding API keys; use environment variables instead.
* Keep shared logic in reusable functions.

## 💡 Biggest Takeaway

> **When working with external systems, always assume something can fail.**

## 🔮 Future Improvements

* Store API keys in environment variables
* Add weather icons or richer formatting
* Add more API data such as humidity and wind
* Improve input validation

## 📈 Roadmap Progress

**11 / 26 projects completed** ✅

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.
