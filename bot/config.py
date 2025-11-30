import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
BRS_API_KEY = os.getenv("BRS_API_KEY")
BRS_API_URL = "https://BrsApi.ir/Api/Market/Gold_Currency.php"
