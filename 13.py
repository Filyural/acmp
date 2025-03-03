a, b = input().split()

bulls = 0
cows = 0

for i in range(4):
    if a[i] == b[i]:
        bulls += 1
for i in range(len(a)):
    if b.count(a[i]) == 1:
        cows += 1
cows -= bulls
print(bulls, cows)