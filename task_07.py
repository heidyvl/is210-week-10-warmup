#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""


DATA = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}


def iter_dict_funky_sum(data):
    """This function returns sum of value minus key"""
    total = 0
    for key, value in data.iteritems():
        total += value - key
    return total
