def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return 'Fizz Buzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input

print(fizz_buzz(1))