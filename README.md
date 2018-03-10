# Currency Converter
two small apps - currency converter CLI and API

## Command Line Applicaion

```
current exchange rates are obtained by forex-python module:
https://github.com/MicroPyramid/forex-python

get forex:
% pip3 install forex-python

usage: currency_converter.py [-h] [-i [INFO]] [--amount AMOUNT]
                             [--output_currency OUT_CURR]
                             [--input_currency IN_CURR] [--file PATH]

optional arguments:
  -h, --help            show this help message and exit
  -i [INFO], --info [INFO]
                        prints out known currencies
  --amount AMOUNT       amount of input currency to be converted, 1.0 if not
                        present
  --output_currency OUT_CURR
                        output currency symbol or code, all known currencies
                        if not present
  --input_currency IN_CURR
                        output currency symbol or code
  --file PATH           output file path

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

CODE   SYMBOL   CURRENCY

'AUD'  [A$]  - Australian dollar
'BRL'  [R$]  - Brazilian real
'BTC'  [Ƀ]   - BitCoin
'CAD'  [C$]  - Canadian dollar
'CHF'  [Fr.] - Swiss franc
'CNY'  [¥]   - Chinese/Yuan renminbi
'CZK'  [Kč]  - Czech koruna
'DKK'  [Kr.] - Danish krone
'EUR'  [€]   - European Euro
'GBP'  [£]   - British pound
'HKD'  [HK$] - Hong Kong dollar
'HRK'  [kn]  - Croatian kuna
'HUF'  [Ft]  - Hungarian forint
'IDR'  [Rp]  - Indonesian rupiah
'ILS'  [₪]   - Israeli new sheqel
'INR'  [₹]   - Indian rupee
'ISK'  [Ikr] - Icelandic króna
'JPY'  [JP¥] - Japanese yen
'KRW'  [₩]   - South Korean won
'MXN'  [M$]  - Mexican peso
'MYR'  [RM]  - Malaysian ringgit
'NOK'  [kr]  - Norwegian krone
'NZD'  [NZ$] - New Zealand dollar
'PHP'  [₱]   - Philippine peso
'PLN'  [zł]  - Polish zloty
'RON'  [L]   - Romanian leu
'RUB'  [₽]   - Russian ruble
'SEK'  [Skr] - Swedish krona
'SGD'  [S$]  - Singapore dollar
'THB'  [฿]   - Thai baht
'TRY'  [₺]   - Turkish new lira
'USD'  [$]   - United States dollar
'ZAR'  [R]   - South African rand


```
