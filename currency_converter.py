"""
Currency converter CLI
python3.5

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


created by Andrej Dravecky
7. 4. 2018

"""

import argparse
import json
from forex_python.converter import CurrencyRates

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


def prepare_parser():
    """
    prepares argument parser for main function

    :return: parser as ArgumentParser object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--amount", type=float, default=1.0, dest="amount")
    parser.add_argument("--output_currency", dest="out_curr")
    parser.add_argument("--file", type= str, dest="path")
    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument("--input_currency", type=str, dest="in_curr", required=True)

    return parser


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


def handler(args):
    """
    handles currency conversion and JSON structure construction

    :param args: parsed arguments
    :return: json structure dump
    """
    input_currency = get_currency(args.in_curr)
    output_currency = get_currency(args.out_curr)

    # creating structured data for JSON structure
    in_data = {"amount": args.amount, "currency": input_currency}
    out_data = CurrencyRates().get_rates(input_currency)
    if output_currency is not None:
        out_data = {output_currency: out_data[output_currency]}

    # recalculate money amount against all rates (round to 2 places after floating point)
    for key in out_data.keys():
        out_data[key] = round(out_data[key] * args.amount, 2)

    return json.dumps({"input": in_data, "output": out_data}, sort_keys=True, indent=4)


def main():
    """
    main function calls parser, handler and handles output

    """
    try:
        args = prepare_parser().parse_args()
        json_dump = handler(args)
        open(args.path, 'w').write(json_dump) if args.path is not None else print(json_dump)

    # catching unrecognized currency exception
    except ValueError as v:
        print(v)


if __name__ == "__main__":
    main()
