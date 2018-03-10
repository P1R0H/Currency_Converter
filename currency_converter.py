"""
Currency Converter CLI
python3.5

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


created by Andrej Dravecky
7. 4. 2018

"""

import argparse
import json
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from forex_python.bitcoin import BtcConverter


# InfoFlag exception, raised when info argument present
class InfoFlag(Exception):
    pass


# Dictionary of symbols and matching currencies, conflicting values use alternative symbols
DICT = {
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
    "Ƀ"  : "BTC",

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


def print_known_currencies():
    """
    currency information print

    """

    rev_dict = {v: k for k, v in DICT.items()}

    print("List of known currencies:", end="\n\n")
    print("CODE   SYMBOL   CURRENCY", end="\n\n")
    c = CurrencyCodes()
    for code in sorted(DICT.values()):
        of = " " * (4 - len(rev_dict[code]))
        print("'{}'  [{}]".format(code, rev_dict[code]), end=of)
        if code == "BTC":
            print("- BitCoin", end="\n")
            continue
        print("- {}".format(c.get_currency_name(code)), end="\n")


def prepare_parser():
    """
    prepares argument parser for main function

    :return: parser as ArgumentParser object

    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--info", dest="info", const=True, default=False,
                        nargs='?', help="prints out known currencies")
    parser.add_argument("--amount", type=float, default=1.0, dest="amount",
                        help="amount of input currency to be converted, 1.0 if not present")
    parser.add_argument("--output_currency", dest="out_curr",
                        help="output currency symbol or code, all known currencies if not present")
    parser.add_argument("--input_currency", type=str, dest="in_curr",
                        help="output currency symbol or code")
    parser.add_argument("--file", type=str, dest="path", help="output file path")

    return parser


def get_currency(arg):
    """
    finds and returns matching currency if found, None otherwise

    :param arg: currency code or symbol
    :return: currency 3-letter code as string

    """

    if arg is None:
        return None
    if arg in DICT.values():
        return arg
    if arg in DICT.keys():
        return DICT[arg]
    raise ValueError("Currency '{}' not recognized".format(arg))


def build_output(amount, inc, outc):
    """
    output data JSON structure builder

    :param amount: amount of currency to be converted
    :param inc: input currency code
    :param outc: output currency code (None if all currencies)
    :return: output JSON structure

    """

    if inc == "BTC":
        # BTC input handling
        if outc is not None:
            return {outc: BtcConverter().convert_btc_to_cur(amount, outc)}

        # BitCoin conversion uses USD rates, amount is changed accordingly
        amount = BtcConverter().convert_btc_to_cur(amount, "USD")
        out_data = CurrencyRates().get_rates("USD")
    else:
        # classic input handling + add BTC
        out_data = CurrencyRates().get_rates(inc)
        out_data["BTC"] = BtcConverter().convert_to_btc(1, inc)

        if outc is not None:
            out_data = {outc: out_data[outc]}

    # recalculate money amount against all rates (round to 5 places after floating point)
    for key in out_data.keys():
        out_data[key] = round(out_data[key] * amount, 5)

    return out_data


def handler(args):
    """
    handles currency conversion and JSON structure construction

    :param args: parsed arguments
    :return: json structure dump

    """

    if args.info:
        raise InfoFlag

    input_currency = get_currency(args.in_curr)
    if input_currency is None:
        raise ValueError("--input_currency parameter has to be present")
    output_currency = get_currency(args.out_curr)

    # creating structured data for JSON structure
    in_data = {"amount": args.amount, "currency": input_currency}
    out_data = build_output(args.amount, input_currency, output_currency)

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
        print("error: ".join(str(v)))

    # catching RateNotAvailable if Forex cannot get rates for whatever reason
    except RatesNotAvailableError as r:
        print("service unavailable".join(str(r)))

    # catching InfoFlag for currency info print
    except InfoFlag:
        print_known_currencies()


if __name__ == "__main__":
    main()
