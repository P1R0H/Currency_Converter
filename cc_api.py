"""
Currency converter API
python3.5

current exchange rates are obtained by forex-python module:
https://github.com/MicroPyramid/forex-python

using Flask webdevelopment framework:
https://github.com/pallets/flask

get forex:
% pip3 install forex-python

get flask
% pip3 install flask

usage:
% python3 cc_api.py
% GET "http://[HOST]:5000/currency_converter?amount=[AMOUNT]&input_currency=[CURRENCY]"
% GET "http://[HOST]:5000/currency_converter?amount=[AMOUNT]&input_currency=[CURRENCY]&output_currency=[CURRENCY]"

[AMOUNT] - defaults to 1, if not present
[CURRENCY] - currency symbol or 3 letter code

created by Andrej Dravecky
7. 4. 2018

"""

from flask import Flask, request, jsonify
from forex_python.converter import CurrencyRates, CurrencyCodes
app = Flask(__name__)

# host address, default = 127.0.0.1
# set to 0.0.0.0 to bind all interfaces
HOST = "127.0.0.1"

# Dictionary of symbols and matching currencies, conflicting values use alternative symbols
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


def get_currency(arg):
    """
    finds and returns matching currency if found, None otherwise

    :param arg: currency code or symbol
    :return: currency 3-letter code as string
     """

    if arg is None:
        return None
    if arg in SYMBOLS.values():
        return arg
    if arg in SYMBOLS.keys():
        return SYMBOLS[arg]
    raise ValueError("Currency '{}' not recognized".format(arg))


@app.route("/currency_converter")
def query_process():
    """
    processes input query and handles currency conversion

    :return: final json structure as json dump

    """
    try:
        amount = float(request.args.get("amount", "1"))
        in_c = get_currency(request.args.get("input_currency"))
        out_c = get_currency(request.args.get("output_currency"))

        # creating structured data for JSON structure
        in_data = {"amount": amount, "currency": in_c}
        out_data = CurrencyRates().get_rates(in_c)
        if out_c is not None:
            out_data = {out_c: out_data[out_c]}

        # recalculate money amount against all rates (round to 2 places after floating point)
        for key in out_data.keys():
            out_data[key] = round(out_data[key] * amount, 2)

        return jsonify({"input": in_data, "output": out_data})

    # catching TypeError from amount conversion to float (should not occur)
    except TypeError as e:
        return jsonify({"error": str(e)})

    # catching ValueError if unrecognized currency
    except ValueError as v:
        return jsonify({"error": str(v)})


if __name__ == "__main__":
    app.run(host=HOST)
