from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from config import TELEGRAM_API_KEY
from price_module import online_price, get_names

# دیکشنری برای ذخیره وضعیت کاربر
user_state = {}


# مرحله اول: نمایش منوی اصلی
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["💰 قیمت ارز", "🥇 قیمت طلا", "💻 قیمت ارز دیجیتال"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("یک دسته انتخاب کنید:", reply_markup=reply_markup)
    user_state[update.effective_chat.id] = "awaiting_category"


# هندلر پیام‌ها
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text

    state = user_state.get(chat_id)

    if state == "awaiting_category":
        # مرحله دوم: نشان دادن اسامی بر اساس دسته
        names = get_names(text)
        if not names:
            await update.message.reply_text("دسته نامعتبر است، دوباره تلاش کنید.")
            return
        keyboard = [[name] for name in names]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "یک مورد انتخاب کنید:", reply_markup=reply_markup
        )
        user_state[chat_id] = {"stage": "awaiting_name", "category": text}

    elif isinstance(state, dict) and state.get("stage") == "awaiting_name":
        # مرحله سوم: نمایش قیمت انتخاب شده
        price_msg = online_price(text)
        await update.message.reply_text(price_msg)

        # بعد از نمایش قیمت، دوباره منوی اصلی را نشان بده
        keyboard = [["💰 قیمت ارز", "🥇 قیمت طلا", "💻 قیمت ارز دیجیتال"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text(
            "یک دسته دیگر انتخاب کنید:", reply_markup=reply_markup
        )
        user_state[chat_id] = "awaiting_category"
    else:
        await update.message.reply_text("لطفا ابتدا /start را بزنید.")


# اجرای ربات
def main():
    app = Application.builder().token(TELEGRAM_API_KEY).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ربات شروع به کار کرد...")
    app.run_polling()


if __name__ == "__main__":
    main()
