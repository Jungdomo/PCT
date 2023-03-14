def solution(topping):
    rst = 0
    key = {}
    cnt = set()
    for i in topping:
        if not key.get(i):
            key[i] = 1
        else:
            key[i] += 1

    for i in topping:
        cnt.add(i)
        key[i] -= 1
        if not key.get(i):
            del (key[i])
        if len(cnt) == len(key):
            rst += 1

    return rst

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))