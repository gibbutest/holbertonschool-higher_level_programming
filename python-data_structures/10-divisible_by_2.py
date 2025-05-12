#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    results = my_list.copy()
    for index, i in enumerate(my_list):
        results[index] = i % 2 == 0
    return results
