# 📱 Telegram Price Bot

A clean, modular Telegram bot that fetches real‑time **currency**, **gold**, and **cryptocurrency** prices using the BRS API.

---

## 🚀 Features
- Live currency prices  
- Gold and cryptocurrency prices  
- Clean user interface with Telegram Reply Keyboards  
- Modular and scalable architecture  
- Fully async (python‑telegram‑bot v20+)

---

## 📁 Project Structure
```
my_telegram_bot/
│
├── bot/
│   ├── main.py          # Entry point
│   ├── handlers.py      # Message handling logic
│   ├── keyboards.py     # Keyboards used in the bot
│   ├── states.py        # User state machine
│   ├── price_module.py  # API data fetching
│   └── config.py        # Environment variables / keys
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/my_telegram_bot
cd my_telegram_bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env`
```
TELEGRAM_API_KEY=YOUR_TELEGRAM_TOKEN
BRS_API_KEY=YOUR_BRS_API_KEY
```

### 4. Run the bot
```bash
python -m bot.main
```

---

## 🤝 Contributing
Pull requests are welcome. The project is fully modular and easy to extend.

---

## 📄 License
MIT License
