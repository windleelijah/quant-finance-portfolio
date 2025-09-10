# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:51:56 2025

@author: windl
"""

import matplotlib.pyplot as plt

def plot_order_book(book):
    bids = sorted([(-p, o.quantity) for p, _, o in book.bids], reverse = True)
    asks = sorted([(p, o.quantity) for p, _, o in book.asks])
    bid_prices, bid_qtys = zip(*bids) if bids else ([],[])
    ask_prices, ask_qtys = zip(*asks) if asks else ([],[])
    
    plt.bar(bid_prices, bid_qtys, color='green', label='Bids')
    plt.bar(ask_prices, ask_qtys, color='red', label='Asks')
    plt.xlabel('Price')
    plt.ylabel('Quantity')
    plt.title('Order Book Depth')
    plt.legend()
    plt.show()
