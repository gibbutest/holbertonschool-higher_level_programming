#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    results = my_list.copy()
    for i in my_list:
        results[i] = i % 2 == 0
    return results
