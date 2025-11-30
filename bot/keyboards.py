from telegram import ReplyKeyboardMarkup

MAIN_MENU = [["💰 قیمت ارز", "🥇 قیمت طلا", "💻 قیمت ارز دیجیتال"]]


def main_menu_keyboard():
    return ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)


def names_keyboard(names: list):
    return ReplyKeyboardMarkup([[name] for name in names], resize_keyboard=True)
