#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for i in new_dic.items():
        new_dic[i[0]] = new_dic[i[0]] * 2
    return new_dic
