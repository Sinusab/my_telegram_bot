import requests
from config import BRS_API_KEY, BRS_API_URL


def online_price(
    current: str, url: str = BRS_API_URL, api_key: str = BRS_API_KEY
) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
    }

    full_url = f"{url}?key={api_key}"

    try:
        response = requests.get(full_url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"خطا در دریافت اطلاعات: {e}"

    data_dict = response.json()
    for item in data_dict.values():
        for thing in item:
            if current == thing["name"]:
                return f"قیمت {thing['name']} در تاریخ {thing['date']} ساعت {thing['time']} برابر است با: {thing['price']} تومان"

    return "ارزی با این نام پیدا نشد."


def get_names(
    category: str, url: str = BRS_API_URL, api_key: str = BRS_API_KEY
) -> list:
    """
    بر اساس دسته بندی (ارز، طلا، ارز دیجیتال) لیست اسامی را برمی‌گرداند
    """
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
    }
    full_url = f"{url}?key={api_key}"
    response = requests.get(full_url, headers=headers)
    data_dict = response.json()

    if category == "💰 قیمت ارز":
        key_name = "currency"
    elif category == "🥇 قیمت طلا":
        key_name = "gold"
    elif category == "💻 قیمت ارز دیجیتال":
        key_name = "cryptocurrency"
    else:
        return []

    return [thing["name"] for thing in data_dict.get(key_name, [])]
