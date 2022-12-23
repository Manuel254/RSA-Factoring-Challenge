#!/usr/bin/python3
import sys
from functools import reduce

"""
This module imports numbers from a file,
finds the prime factors of each number and then prints
the product of two large factors.

  Example:
    n = 4
    n=p*q
    4=2*2
"""

def prime_fact(number, prime_factors):
  divisor = 2

  if number == 1:
    return prime_factors

  while number % divisor != 0:
    divisor += 1

  prime_factors.append(divisor)
  prime_fact(number/divisor, prime_factors)
  return prime_factors


def natural_nums():
  factors = []
  prime_factors = []
  with open(sys.argv[1], 'r') as f:
    for number in f:
      factors.append(prime_fact(int(number), prime_factors))
      prime_factors = []
  return factors

def print_factorization():
  for prime_list in natural_nums():
    if len(prime_list) == 1:
      p = prime_list[0]
      q = 1
    elif len(prime_list) == 2:
      p = prime_list[0]
      q = prime_list[1]
    elif len(prime_list) > 2:
      ind_min = prime_list.index(min(prime_list))
      q = prime_list.pop(ind_min)
      p = reduce(lambda x, y: x * y, prime_list)

    prod = p * q
    print(f"{prod}={p}*{q}")

print_factorization()
