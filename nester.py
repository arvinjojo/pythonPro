# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def print_lol(the_list, indent = False, level=0):
    """Says"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                for tap_stop in range(level):
                    print("\t", end = '')
            print(each_item)
    
"""movie = ["假装爱情", ["黄渤", "江一燕", ["光头", "张国立子"]], 120]

print_lol(movie)"""