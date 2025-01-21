a = input()
if len(a) == 1:
    print('25')
else:
    n = int(a[:-1])
    res = n * (n + 1)
    print(str(res) + '25')