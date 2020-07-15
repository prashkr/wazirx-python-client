from entry import Entry


class Orderbook:
    def __init__(self):
        self.bids = []
        self.asks = []

    def init(self, wx_orderbook: dict):
        """
        Initializes bids sorted in desc and asks sorted in asc
            bids: high to low
            asks: low to high
        """
        for p, q in wx_orderbook['bids']:
            self.bids.append(Entry(p, q))

        for p, q in wx_orderbook['asks']:
            self.asks.append(Entry(p, q))

    @property
    def spread(self):
        highest_buy_entry, lowest_sell_entry = self.bids[0], self.asks[0]
        return lowest_sell_entry.price - highest_buy_entry.price
