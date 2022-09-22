import math
from itertools import ifilter

def sieve(n):
    """Returns a list holding prime numbers, upto but not including n"""
    # I mean, we could just download a list of primes instead. That would be more performant time and memory wise for large n
    n = int(n)
    if n <= 1:
        return []
    prime_flag_table = [False for _ in range(2)]
    prime_flag_table.extend([True for _ in range(2, n)]) 
    true_values_table_it = ifilter(lambda i: prime_flag_table[i], range(2, int(math.ceil(math.sqrt(n)))))
    for i in true_values_table_it:
        for j in range(i**2, n, i):
            prime_flag_table[j] = False
    primes = [idx for idx, value in enumerate(prime_flag_table) if value]
    return primes

def prime_string(length):
    s = ""
    # we want to underestimate the number of primes in a range so we don't need to start the sieve over again
    # for more, read https://en.wikipedia.org/wiki/Prime_number_theorem#Table_of_%CF%80(x),_x_/_log_x,_and_li(x)
    factor = 1.5
    reasonable_min = 20 + length # 235711
    estimate_needed =  length/math.log(max(2, length))
    while len(s) < length:
        primes = sieve(factor * max(reasonable_min, estimate_needed)) 
        s = list_to_string(primes)
        factor *= 2
    return s[:length]

def list_to_string(l):
    return ''.join([str(n) for n in l])


ID_length = 5

def solution(n):
    prime_s = prime_string(n + ID_length) 
    return prime_s[n:(n+ID_length)]


def test(n):
    s = solution(n)
    print(s, len(s) == ID_length, n)