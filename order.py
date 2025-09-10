# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 12:58:48 2025

@author: windl
"""

from dataclasses import dataclass
import time

@dataclass(order=True)
class Order:
    timestamp: float
    order_id: int
    side: str       
    price: float
    quantity: int