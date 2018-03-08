# Currency Converter
two small apps - currency converter CLI and API

## Command Line Applicaion

```
current exchange rates are obtained by forex-python module:
https://github.com/MicroPyramid/forex-python

get forex:
% pip3 install forex-python

usage: currency_converter.py [-h] [-i [INFO]] [--amount AMOUNT]
                             [--output_currency OUT_CURR] [--file PATH]
                             --input_currency IN_CURR

optional arguments:
  -h, --help            show this help message and exit
  -i [INFO], --info [INFO]
                        prints out known currencies
  --amount AMOUNT       amount of input currency to be converted, 1.0 if not
                        present
  --output_currency OUT_CURR
                        output currency symbol or code, all known currencies
                        if not present
  --file PATH           output file path

required named arguments:
  --input_currency IN_CURR
                        output currency symbol or code

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
List of known currencies:

'AUD' - Australian dollar
'BRL' - Brazilian real
'CAD' - Canadian dollar
'CHF' - Swiss franc
'CNY' - Chinese/Yuan renminbi
'CZK' - Czech koruna
'DKK' - Danish krone
'EUR' - European Euro
'GBP' - British pound
'HKD' - Hong Kong dollar
'HRK' - Croatian kuna
'HUF' - Hungarian forint
'IDR' - Indonesian rupiah
'ILS' - Israeli new sheqel
'INR' - Indian rupee
'ISK' - Icelandic króna
'JPY' - Japanese yen
'KRW' - South Korean won
'MXN' - Mexican peso
'MYR' - Malaysian ringgit
'NOK' - Norwegian krone
'NZD' - New Zealand dollar
'PHP' - Philippine peso
'PLN' - Polish zloty
'RON' - Romanian leu
'RUB' - Russian ruble
'SEK' - Swedish krona
'SGD' - Singapore dollar
'THB' - Thai baht
'TRY' - Turkish new lira
'USD' - United States dollar
'ZAR' - South African rand

```
