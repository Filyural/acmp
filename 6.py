try:
    n, m = input().split('-')
    x1 = ord(n[0]) - 64
    y1 = int(n[1])
    x2 = ord(m[0]) - 64
    y2 = int(m[1])

    if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("ERROR")
except:
    print("ERROR")
