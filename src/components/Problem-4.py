l = list(map(int, input().split(",")))
d = {}
for i in range(1, 10):
    cnt = 0
    for j in l:
        if j % i == 0:
            cnt += 1
    d[i] = cnt
print(d)
