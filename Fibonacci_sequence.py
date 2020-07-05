# from functools import lru_cache


# @lru_cache(maxsize=None)
# def fib4(n: int) -> int:  # same definition as fib2()
#     if n < 2:  # base case
#         return n
#     return fib4(n - 2) + fib4(n - 1)  # recursive case


from typing import Generator


def fib6(n: int) -> Generator[int, None, None]:
    yield 0  # special case

    if n > 0:
        yield 1  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)

    for _ in range(1, n):
        last, next = next, last + next
        yield next  # main generation step


if __name__ == "__main__":
    for i in fib6(50):
        print(i)

# if __name__ == "__main__":
#     print(fib4(5))
#     print(fib4(50))
