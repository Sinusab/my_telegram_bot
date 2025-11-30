from telegram import Update
from telegram.ext import ContextTypes
from .states import user_state, AWAITING_CATEGORY, AWAITING_NAME
from .keyboards import main_menu_keyboard, names_keyboard
from .price_module import online_price, get_names


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("یک دسته انتخاب کنید:", reply_markup=main_menu_keyboard())
    user_state[update.effective_chat.id] = AWAITING_CATEGORY


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text

    state = user_state.get(chat_id)

    # مرحله ۱ — انتخاب دسته
    if state == AWAITING_CATEGORY:
        names = get_names(text)
        if not names:
            await update.message.reply_text("❌ دسته نامعتبر است، دوباره تلاش کنید.")
            return

        await update.message.reply_text("یک مورد انتخاب کنید:", reply_markup=names_keyboard(names))
        user_state[chat_id] = {"stage": AWAITING_NAME, "category": text}

    # مرحله ۲ — انتخاب آیتم
    elif isinstance(state, dict) and state.get("stage") == AWAITING_NAME:
        msg = online_price(text)
        await update.message.reply_text(msg)

        await update.message.reply_text("یک دسته دیگر انتخاب کنید:", reply_markup=main_menu_keyboard())
        user_state[chat_id] = AWAITING_CATEGORY

    else:
        await update.message.reply_text("لطفا ابتدا /start را بزنید.")
