import math
from itertools import ifilter


def sieve(n, prime_flag_table = []):
    """Returns a list holding prime numbers"""
    # I mean, we could just download a list of primes instead. That would be more performant time and memory wise for large n
    if prime_flag_table == []:
        prime_flag_table = [True for _ in range(n + 1)]
        prime_flag_table[0] = prime_flag_table[1] = False
    else:
        prime_flag_table.extend([True for _ in range(len(prime_flag_table), n + 1)]) 
    true_values_table_it = ifilter(lambda i: prime_flag_table[i], range(2, int(math.sqrt(n))))
    for i in true_values_table_it:
        for j in range(i**2, n + 1, i):
            prime_flag_table[j] = False
    primes = [idx for idx, value in enumerate(prime_flag_table) if value]
    return primes

def prime_string(length):
    s = ""
    factor = 2
    primes = []
    while len(s) < length:
        reasonable_min = 20 + length # 235711131719
        PNT_dist = length/math.log(max(2, length)) # see "Prime number theorem"
        primes = sieve(factor * max(reasonable_min, PNT_dist), primes) 
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