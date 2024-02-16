import json
import time

import pandas as pd

from Kraken import KrakenAPI
from Math import Johansen
from Math.Johansen import johansen


def main():
    # api = KrakenAPI()
    # data = api.get_asset_info("XDG")
    # data = data["result"]
    # data = pd.DataFrame(data)
    # print(data)
    # data.to_excel("price_data.xlsx")

    # data = api.get_tradable_asset_pairs("BTC", "CAD")

    # data = api.get_ohlc_data("XBTUSD", 60, 1707505232)
    # print(data)
    johansen("dummy")


main()

# get the price of a given crypto and output to excel
# def get_price_and_output_to_excel(ticker, output_file):
#     data = api.get_daily_prices(ticker)
#     df = pd.DataFrame(data)
#     df.to_excel(output_file)

# if __name__ == "__main__":
#     api = AlphaVantageAPI()
#     api.get_daily_prices("BTC")

#     # read list of cryptos from a file
#     digital_curr_file = "digital_currency_list.csv"
#     currency_df = pd.read_csv(digital_curr_file)
#     currency_list = currency_df.to_dict()
#     currency_list = currency_list["currency code"]

# get list of all cryptos and output to same file
# i = 0
# while i<len(currency_list):
# while i < 3:
#     get_price_and_output_to_excel(currency_list[84], "price_data.xlsx")
#     i += 1

# get_price_and_output_to_excel("BTC", "price_data.xlsx")


# if __name__ == "__main__":
#     api = CoinGeckoApi()

#     # pull data for an individual coin

#     # data = api.get_ohlc("bitcoin")
#     # fp = "price_data.xlsx"
#     # df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close"])
#     # df["Date"] = pd.to_datetime(df["Date"], unit="ms")
#     # df.to_excel("price_data.xlsx")

#     df_markets = pd.DataFrame(api.markets())
#     coins = ["bitcoin", "ethereum", "tether"]

#     excel_writer = pd.ExcelWriter("price_data.xlsx", engine="xlsxwriter")
#     count = 100

#     for id in df_markets["id"]:
#         print("pulling data for", id, " ", count, " more to go")
#         count -= 1
#         curr_data = api.get_ohlc(id)
#         curr_df = pd.DataFrame(
#             curr_data, columns=["Date", "Open", "High", "Low", "Close"]
#         )
#         curr_df["Date"] = pd.to_datetime(curr_df["Date"], unit="ms")
#         sheet_name = f"{id}"
#         curr_df.to_excel(excel_writer, sheet_name=sheet_name, index=False)
#         time.sleep(20)

#     excel_writer.save()
