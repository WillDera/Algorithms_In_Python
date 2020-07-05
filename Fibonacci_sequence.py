# Introducing memotization
from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # Our base cases


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)  # memotization
    return memo[n]
    # return fib(n - 2) + fib(n - 1)  # recursive case


if __name__ == "__main__":
    print(fib(5))
    print(fib(50))
