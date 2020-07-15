import time
import requests
from pprint import pprint


def timeit(method):
    """
    Use this decorator to debug running time of any method.
    Usage:
        Add @timeit on top of the function you want to time
    """
    def timed(*args, **kw):
        t_start = time.time()
        result = method(*args, **kw)
        t_end = time.time()
        print('{}: {}ms'.format(method.__name__, (t_end - t_start) * 1000))
        return result
    return timed


class WazirX:
    def __init__(self,
                 url='https://api.wazirx.com',
                 key='xxxx',
                 secret='xxxx'):
        self.url = url
        self.key = key
        self.secret = secret

    def do_get(self, url):
        response = requests.get(url)
        data = response.json()
        # pprint(data)
        return data

    def get_market_status(self):
        url = self.url + '/api/v2/market-status'
        return self.do_get(url)

    def get_market_ticker(self):
        url = self.url + '/api/v2/tickers'
        return self.do_get(url)

    def get_orderbook(self, market):
        url = self.url + '/api/v2/depth?market=' + market
        return self.do_get(url)

    def get_market_trade_history(self, market):
        url = self.url + '/api/v2/trades?market=' + market
        return self.do_get(url)
