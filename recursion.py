#!user/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(n):
    """fibonacci sequence with recursion"""
    if n < 2: # return 0 or 1 if 0 or 1
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    """Find GCD of two numbers using Euclid’s GCD Algorithm"""
    if b > a:
        a, b = b, a # Avoid 0 division error if b is a greater number than a

    if a % b == 0:
        return b

    return gcd(b, a % b)

def compareTo(s1, s2):
    




