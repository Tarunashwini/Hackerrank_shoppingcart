#!/bin/python3

import math
import os
import random
import re
import sys



class Item:
    # Define the constructor
    def _init_(self, n='', p=0):  
        self.name = n  
        self.price = p 
    def give_item(self):
        return self.name, self.price


class ShoppingCart:
    def _init_(self, name0='', price0=0):
        self.nameI = name0
        self.priceI = price0
        self.name_list = []
        self.price_list = []
    
    def call_Item(self, item):
        nout, pout = Item.give_item(item)
        # print('nout: ', nout)
        # print('pout: ', pout)
        return nout, pout
    
    # Append items to the shopping cart
    def add(self, item):
        nout, pout = self.call_Item(item)
        print('Current Proce ', priceI)
        self.name_list = self.name_list + [nout]
        print('Your cart contains: ', self.name_list)
        
        self.price_list = self.price_list + [pout]
        print('Price list of items in cart: ', self.price_list)
        return self.name_list, self.price_list
    
    def total(self):
        self.price_list = list(map(int,self.price_list))
        tot_out = sum(self.price_list)
        print('Total shopping cart: ', tot_out)
        print(tot_out)
        return tot_out
        
    def num_of_cartitems(self):
        num_items = len(self.name_list)
        print(num_items)
        return num_items
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(cart.num_of_cartitems()) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            name, price = item.give_item(name, price)
            cart.add(name, price)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()