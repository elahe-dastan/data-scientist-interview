def digits_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


def solution(n: int) -> int:
    a = 0  # even squence
    b = 1  # odd squence
    for i in range(2, n):
        if i % 2 == 0:
            a = digits_sum(a) + digits_sum(b)
        else:
            b = digits_sum(a) + digits_sum(b)
    if n % 2 == 0:
        return a
    return b


if __name__ == "__main__":
    assert digits_sum(13) == 4
    assert digits_sum(12) == 3
    assert digits_sum(8) == 8

    assert solution(7) == 13
    assert solution(8) == 12
    assert solution(9) == 7
