# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:23:13 2025

@author: windl
"""

import heapq
from collections import deque

class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []
        self.order_id_counter = 0
        
    def add_order(self, side, price, quantity):
        self.order_id_counter += 1
        timestamp = time.time()
        order = Order(timestamp, self.order_id_counter, side, price, quantity)
        if side == 'buy':
            heapq.heappush(self.bids, (-price, timestamp, order))
        else:
            heapq.heappush(self.asks, (price, timestamp, order))
        self.match_orders()
        
    def match_orders(self):
        while self.bids and self.asks:
            best_bid = self.bids[0][2]
            best_ask = self.asks[0][2]
            if best_bid.price >= best_ask.price:
                trade_qty = min(best_bid.quantity, best_ask.quantity)
                print(f"Trade: {trade_qty} @ {best_ask.price}")
                best_bid.quantity -= trade_qty
                best_ask.quantity -= trade_qty
                if best_bid.quantity == 0:
                    heapq.heapop(self.bids)
                if best_ask.quantity == 0:
                    heapq.heapop(self.asks)
            else:
                break
