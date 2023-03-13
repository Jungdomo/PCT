def solution(k, tangerine):
    key = {}
    rst = []
    a = 0
    for i in tangerine:
        if not key.get(i):
            key[i] = 1
        else:
            key[i] += 1

    for i in key:
        rst.append(key.get(i))
    rst.sort(reverse=True)

    for i in rst:
        k = k - i
        a += 1
        if k <= 0:
            break

    return a

print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))