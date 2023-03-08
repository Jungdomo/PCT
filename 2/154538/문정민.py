def solution(x, y, n):
    s = set()
    s.add(x)
    cnt = 0

    while s:
        if y in s:
            return cnt
        tst = set()
        for i in s:
            if i*2 <= y:
                tst.add(i*2)
            if i*3 <= y:
                tst.add(i*3)
            if i+n <= y:
                tst.add(i+n)
        s = tst
        cnt += 1
    return -1

print(solution(10, 40, 5))