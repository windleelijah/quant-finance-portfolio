# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:50:24 2025

@author: windl
"""

from order_book import OrderBook

book = OrderBook()
book.add_order('buy', 100.0, 10)
book.add_order('sell',99.5,5)
book.add_order('sell', 100.0, 10)
book.add_order('buy',101.0,5)
