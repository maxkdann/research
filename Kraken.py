import json

import pandas as pd
import requests

import constants.defs as defs


class KrakenAPI:
    def __init__(self):
        self.session = requests.Session()

    def make_request(
        self, url, verb="get", code=200, params=None, data=None, headers=None
    ):
        full_url = f"{defs.KRAKEN_URL}/{url}"

        if data is not None:
            data = json.dumps(data)

        try:
            response = None
            if verb == "get":
                response = self.session.get(
                    full_url, params=params, data=data, headers=headers
                )
            if verb == "post":
                response = self.session.post(
                    full_url, params=params, data=data, headers=headers
                )
            if verb == "put":
                response = self.session.put(
                    full_url, params=params, data=data, headers=headers
                )

            if response == None:
                # haven't made a request
                return False, {"error": "verb not found"}

            # otherwise we've got something back
            if response.status_code == code:
                return True, response.json()
            else:
                return False, response.json()
        except Exception as error:
            return False, {"Exception": error}

    def get_daily_prices(self, symbol):
        url = f"query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=CAD&apikey={defs.ALPHA_API_KEY}"
        ok, data = self.make_request(url)
        if ok:
            return data
        else:
            print("ERROR get_daily_prices()", data)
            return None

    def get_asset_info(self, assets=None):
        """
        Get a list of all tradeable assets
        """
        if assets == None:
            url = "Assets"
        else:
            url = f"Assets?asset={assets}"
        ok, data = self.make_request(url)
        if ok:
            return data
        else:
            return ok, "ERROR get_asset_info"

    def get_tradable_asset_pairs(self, currency1, currency2):
        """
        Get information about a specific coin pair
        Gives you the fees you pay based on the volume for maker/taker
        Also gives you when you get margin called, the order minimum
        """
        url = f"AssetPairs?pair={currency1}/{currency2}"
        ok, data = self.make_request(url)
        if ok:
            return data
        else:
            return "ERROR get_asset_info"

    def get_ohlc_data(self, pair, interval, since):
        """
        pair = "BTCUSD"
        interval = 1,5,15,30,60,240,1440,10080,21600 minutes
        since = EPOCH timestamp
        gives you 720 data points since the since data
        """
        url = f"OHLC?pair={pair}?interval={interval}?since={since}"
        ok, data = self.make_request(url)
        if ok:
            return data
        else:
            return "ERROR get_ohlc_data"
