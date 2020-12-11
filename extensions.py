import requests
import json
from config import *


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'It is impossible to convert the same currency {base}.')
        
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'It is impossible to process the currency {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'It is mpossible to process the currency {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'It is impossible to convert an amount of {amount}')
        
        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&symbols={base_ticker}')
        total_base=json.loads(r.content)["rates"][keys[base]]
        
        return total_base
