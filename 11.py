k, n = map(int, input().split())
steps = [1]
for i in range(1, n + 1):
    res = 0
    for j in range(1, k + 1):
        if i - j >= 0:
            res += steps[i - j]
    steps.append(res)
print(steps[-1])

