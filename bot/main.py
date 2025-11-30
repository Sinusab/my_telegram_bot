from telegram.ext import Application, CommandHandler, MessageHandler, filters
from .config import TELEGRAM_API_KEY
from .handlers import start, handle_message


def main():
    app = Application.builder().token(TELEGRAM_API_KEY).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
