import requests
import datetime
from datetime import datetime


def get_currency():
    # API ключ оставлен намеренно, для простоты тестирования кода.
    api_key = "dea272e9412a4d18810b446111a48ee8"
    base_currency = "USD"
    target_currency = "RUB"
    url = f"https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        exchange_rate = data["rates"][target_currency]

        return {"exchange_rate": exchange_rate, "date": datetime.now().isoformat()}
    else:
        return {
            "error": f"Ошибка при получении данных. Код ошибки: {response.status_code}"
        }
