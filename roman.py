def roman(num):
    roman_numbers = {       # 1
        1: "I",
        5: "V",
        10: "X",
        50: "L", 
        100: "C",
        500: "D",
        1000: "M",
    }
    result = ""
    remainder = num

    for i in sorted(roman_numbers.keys(), reverse=True):# 2
        if remainder > 0:
            multiplier = i
            roman_digit = roman_numbers[i]

            times = remainder // multiplier         # 3
            remainder = remainder % multiplier      # 4
            result += roman_digit * times           # 4

    return result


print(roman(2022))