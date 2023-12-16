from itertools import count, islice
from math import prod

def M(N):
    divisors = []
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            divisors.append(i)
            if len(divisors) == 5:
                break
    if len(divisors) < 5:
        return 0
    else:
        return prod(divisors)

def find_numbers():
    numbers = []
    for n in islice(count(200000001), None):
        m = M(n)
        if 0 < m and m < n:
            numbers.append((n, m))
            if len(numbers) == 5:
                break
    return sorted(numbers, key=lambda x: x[0])

result = find_numbers()
for n, m in result:
    print(f"M({n}) = {m}")