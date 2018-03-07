# Currency Converter
two small apps - currency converter CLI and API

## Command Line Applicaion

```
current exchange rates are obtained by forex-python module:
https://github.com/MicroPyramid/forex-python

get forex:
% pip3 install forex-python

usage: currency_converter.py [-h] [--amount AMOUNT]
                             [--output_currency OUT_CURR] [--file PATH]
                             --input_currency IN_CURR

optional arguments:
  -h, --help            show this help message and exit
  --amount AMOUNT
  --output_currency OUT_CURR
  --file PATH

required named arguments:
  --input_currency IN_CURR
```

## Web API
```
using Flask webdevelopment framework:
https://github.com/pallets/flask

get flask:
% pip3 install flask

usage:
% python3 cc_api.py
% GET "http://[HOST]:5000/currency_converter?amount=[AMOUNT]&input_currency=[CURRENCY]"
% GET "http://[HOST]:5000/currency_converter?amount=[AMOUNT]&input_currency=[CURRENCY]&output_currency=[CURRENCY]"

[AMOUNT] - defaults to 1, if not present
[CURRENCY] - currency symbol or 3 letter code
```

## Symbols and Currensies
```
SYMBOLS = {
        "$"  : "USD",
        "kr" : "NOK",
        "¥"  : "CNY",
        "₪"  : "ILS",
        "₹"  : "INR",
        "R$" : "BRL",
        "Kr.": "DKK",
        "₺"  : "TRY",
        "L"  : "RON",
        "zł" : "PLN",
        "฿"  : "THB",
        "Kč" : "CZK",
        "RM" : "MYR",
        "Fr.": "CHF",
        "€"  : "EUR",
        "S$" : "SGD",
        "R"  : "ZAR",
        "£"  : "GBP",
        "₽"  : "RUB",
        "Rp" : "IDR",
        "₩"  : "KRW",
        "kn" : "HRK",
        "Ft" : "HUF",
        "₱"  : "PHP",

        # alternative symbols

        "A$" : "AUD",
        "M$" : "MXN",
        "C$" : "CAD",
        "NZ$": "NZD",
        "HK$": "HKD",
        "JP¥": "JPY",
        "Ikr": "ISK",
        "Skr": "SEK"
    }

```
