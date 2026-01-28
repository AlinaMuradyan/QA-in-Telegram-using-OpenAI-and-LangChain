# QA Telegram Bot using OpenAI & LangChain

This project is a simple **Question-Answering Telegram bot** built with **Python**, **LangChain**, and **OpenAI**.  
The bot answers user questions and keeps **separate conversation memory per Telegram user**.

---

## 🚀 Features

- Telegram bot interface
- Uses OpenAI chat models via LangChain
- Deterministic responses (`temperature = 0`)
- Per-user conversation memory (each user has their own context)
- Simple and clean project structure

---

## 📁 Project Structure

```

.
├── model.py          # LangChain QA logic with memory
├── telegram.py       # Telegram bot logic
├── requirements.txt  # Project dependencies

````

---

## ⚙️ Requirements

- Python **3.9+**
- A Telegram Bot Token
- An OpenAI API Key

---

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/AlinaMuradyan/QA-in-Telegram-using-OpenAI-and-LangChain.git
cd QA-in-Telegram-using-OpenAI-and-LangChain
````

2. **Create a virtual environment (recommended)**

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration (IMPORTANT)

You **must create a `config.py` file** in the project root.

### `config.py`

```python
TELEGRAM_TOKEN = "your_telegram_bot_token_here"
OPENAI_API_KEY = "your_openai_api_key_here"
```

❗ This file is **not included** in the repository and **must not be committed**.

---

## ▶️ Running the Bot

Start the Telegram bot with:

```bash
python telegram.py
```

Open Telegram, find your bot, and start chatting 🚀

---

## 🧠 How Memory Works

* Each Telegram user has **their own conversation memory**
* The bot remembers context **only for that specific user**
* Different users do **not** share memory

---

## 🛡️ Notes

* Do **not** expose your API keys
* Do **not** commit `config.py`
* This project is intended for **learning and experimentation**

---

## 📜 License

This project is provided for educational purposes.
