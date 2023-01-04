def solution(s):
    a = list(map(str, s))

    first = "aaa"

    x = 0
    y = 0

    f = 0
    l = 0

    check = []

    for i in a:
        if first == "aaa":
            x = y
            first = i
            f += 1
        elif first == i:
            f += 1
        elif first != i:
            l += 1

        if f == l:
            check.append(a[x:y])
            first = "aaa"
            f = 0
            l = 0

        if f != l:
            if y == len(a)-1:
                check.append('sss')

        y += 1

    return len(check)

print(solution("abracadabra"))