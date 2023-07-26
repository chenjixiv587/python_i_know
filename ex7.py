from functools import partial


def pow(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s


power_2 = partial(pow, n=2)
power_2(2)
print(power_2(2))
