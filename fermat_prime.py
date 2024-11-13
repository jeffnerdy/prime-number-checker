import math

# Multiply two integers with respect to a modulo
def multiply_mod(a, b, modulo):
    result = 0
    a = a % modulo
    while b > 0:
        if b % 2 == 1:
            result = (result + a) % modulo
        a = (a * 2) % modulo
        b //= 2
    return result

# Reduce a large exponent with respect to a modulo
def reduce_exp(base, exponent, modulo):
    result = 1
    base = base % modulo
    while exponent > 0:
        if exponent % 2 == 1:
            #Without this function the multiplication would overflow if the operands are very large
            result = multiply_mod(result, base, modulo)
        base = multiply_mod(base, base, modulo)
        exponent //= 2
    return result

# Check if an integer is prime following Fermat's theorem
def is_prime(number):
    result = reduce_exp(2, number - 1, number)
    return result % number == 1
