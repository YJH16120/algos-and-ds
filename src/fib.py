"""
Find the nth term of a fibonacci sequence.
1, 1, 2, 3, 5, 8, 13, 21, ...
if n = 6, return 8. Since 8 is the 6th position in the sequence
"""

def fib(n, memo = {}):
    if n in memo:
        return memo[n]

    elif n <= 2:
        return 1

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

out = fib(6)
print(out)