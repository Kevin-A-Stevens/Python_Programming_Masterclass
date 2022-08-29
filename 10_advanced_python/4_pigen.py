"""
create a generator to calculate odd numbers

Use that odd number generator to calculate pi
"""


def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = oddnumbers()
    approx = 0
    while True:
        approx += (4 / next(odds))
        yield approx
        approx -= (4 / next(odds))
        yield approx


approx_pi = pi_series()

for x in range(10000000):
    print(next(approx_pi))




