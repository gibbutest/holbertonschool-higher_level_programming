#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) and not None:
        return 0
    elif not roman_string:
        return None

    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for i in range(len(roman_string) - 1, -1, -1):
        curr_value = roman_map[roman_string[i]]

        if curr_value < prev_value:
            result -= curr_value
        else:
            result += curr_value

        prev_value = curr_value
    return result
