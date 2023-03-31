def solution(name, yearning, photo):
    key = {}
    for i in range(len(name)):
        key[name[i]] = yearning[i]
    rst = []

    for i in photo:
        check = 0
        for j in i:
            if key.get(j) is None:
                continue
            check += key.get(j)
        rst.append(check)

    return rst

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))