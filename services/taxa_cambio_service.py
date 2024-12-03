import requests

API_KEY = "beadbdedf769d9911ba30928"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

def obter_taxas_cambio():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()['conversion_rates']
    else:
        raise Exception("Falha ao obter taxas de câmbio")