n = int(input())
counter = 0
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if j > i and arr[j] == 1:
            counter += 1
print(counter)