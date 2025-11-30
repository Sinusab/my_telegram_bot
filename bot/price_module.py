import requests
from .config import BRS_API_KEY, BRS_API_URL


def fetch_data():
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"{BRS_API_URL}?key={BRS_API_KEY}"

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def online_price(name: str) -> str:
    try:
        data = fetch_data()
    except Exception as e:
        return f"❌ خطا در دریافت اطلاعات: {e}"

    for category_items in data.values():
        for thing in category_items:
            if name == thing["name"]:
                return (
                    f"📌 قیمت {thing['name']}\n"
                    f"📅 تاریخ: {thing['date']}  ⏰ ساعت: {thing['time']}\n"
                    f"💵 قیمت: {thing['price']} تومان"
                )

    return "❌ موردی با این نام پیدا نشد."


def get_names(category: str) -> list:
    try:
        data = fetch_data()
    except Exception:
        return []

    mapping = {
        "💰 قیمت ارز": "currency",
        "🥇 قیمت طلا": "gold",
        "💻 قیمت ارز دیجیتال": "cryptocurrency",
    }

    key = mapping.get(category)
    if not key:
        return []

    return [item["name"] for item in data.get(key, [])]
