def solution(storey):
    a = list(map(int, str(storey)))
    a.reverse()

    x = 0
    rst = 0

    for i in a:
        if x == len(a)-1:
            if i >= 6:
                rst += 10 - i + 1
            elif i <= 5:
                rst += i
        elif i >= 6:
            a[x+1] += 1
            rst += 10 - i
        elif i <= 4:
            rst += i
        elif i == 5:
            if a[x + 1] >= 5:
                a[x + 1] += 1
                rst += 10 - i
            else:
                rst += i

        x += 1

    return rst
