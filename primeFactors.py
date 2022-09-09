def get_prime_factor(num):
    factor = list()
    divisor = 2
    while(divisor <= num):
        if(num % divisor) == 0:
            factor.append(divisor)
            num = num // divisor
        else:
            divisor +=1
    return factor


print(get_prime_factor(250))
