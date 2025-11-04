def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib_memo(n - 2) + fib_memo(n - 1)