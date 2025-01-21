a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

res_arr = []

for x in range(-100, 101):
    if a * x ** 3 + b * x ** 2 + c * x + d == 0:
        res_arr.append(x)

print(*res_arr)