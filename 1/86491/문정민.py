def solution(sizes):

    a = 0
    for i in sizes[:]:
        if sizes[a][0] != max(i):
            cnt = min(i)
            sizes[a][0] = max(i)
            sizes[a][1] = cnt
        a += 1

    ma = []
    mi = []

    for i in sizes:
        ma.append(i[0])
        mi.append(i[1])

    return max(ma) * max(mi)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))