from client import WazirX
from orderbook import Orderbook


wx = WazirX()


def compute_spread(market):
    wx_ob = wx.get_orderbook(market=market)
    ob = Orderbook()
    ob.init(wx_orderbook=wx_ob)
    print(f'spread for market: {market} is {ob.spread}')


while True:
    compute_spread(market='btcinr')
    compute_spread(market='ethinr')
