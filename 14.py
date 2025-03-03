def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


a, b = map(int, input().split())
print(a * b // gcd(a, b))
