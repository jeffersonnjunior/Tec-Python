import requests
from app.exceptions import InvalidCepError

def get_address_by_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code != 200:
        raise InvalidCepError(cep)
    return response.json()