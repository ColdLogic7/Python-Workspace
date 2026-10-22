# 💱 Currency Converter CLI

A Python command-line tool that converts currencies using live exchange rates from ExchangeRate-API. It uses terminal arguments instead of interactive input loops.

## ✨ Features

- 💱 Convert between supported currencies
- 🌍 Choose source and target currencies
- 📋 List available currency codes and rates
- ⚙️ Configure conversions using command-line arguments
- ⚠️ Validate inputs and handle API errors

## 🛠 Skills Practiced

- `argparse` and command-line arguments
- REST API requests using `requests`
- API key authentication through URLs
- Input validation and explicit Boolean returns
- Dependency passing and reusable functions
- JSON response handling and exception management

## 🚀 How To Run

```bash
pip install requests
python Currency_Converter.py --amount 100 --from USD --to INR
```

List available currencies:

```bash
python Currency_Converter.py --list
```

Replace the placeholder API key in the script with your ExchangeRate-API key. Avoid publishing real API keys on GitHub.

## 📂 Project Structure

```text
Currency-Converter/
├── Currency_Converter.py
└── README.md
```

## 📚 What I Learned — Project 13

- Use `argparse` to build a proper CLI interface with required arguments, defaults, and Boolean flags.
- Fetch exchange rates once in `main()` and pass the data to other functions.
- Check both HTTP status codes and API-level error messages.
- Make validation functions return clear `True` or `False` results.
- Follow API documentation to implement the correct authentication method.

## ⚠️ Lessons Worth Remembering

- Small typos can cause silent bugs without raising exceptions.
- Check external data before accessing its fields.
- Avoid repeating the same API request across multiple functions.
- A function's return value must clearly communicate its outcome.

## 💡 Biggest Takeaway

> **Build the interface around the task: a CLI tool can run once, do its job, and exit without an interactive loop.**

## 🔮 Future Improvements

- Move the API key to an environment variable.
- Add currency-code autocomplete or suggestions.
- Improve error handling for invalid API responses.
- Add automated tests for conversion and validation logic.

## 📈 Roadmap Progress

**13 / 26 projects completed** ✅

## 👨‍💻 Author

**ColdLogic7**

Learning Python through project-based practice and documenting lessons learned after every project.