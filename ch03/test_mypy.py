from typing import List

# EX1) ERROR
ans: List[int] = [1, 2, 3, 4]
wrong: List[int] = ["1", "2", "3", "4"]

# EX2) ERROR


def add1(n1: str, n2: int) -> int:
    return (n1+n2)


print(add1(1, 2))

# EX3) PASS


def add2(n1, n2: int) -> int:
    return (n1+n2)


print(add2(1, 2))

# EX4) PASS...🤔


def add3(n1, n2: int) -> int:
    return (n1+n2)


print(add3("1", 2))
