def solution(s, skip, index):
    a = list(s)
    b = list(skip)

    result = []

    for i in a:
        rst = i
        for j in range(index):
            if ord(rst) + 1 == 123:
                rst = 'a'
            else:
                rst = chr(ord(rst) + 1)

            for v in b:
                if rst in b:
                    if ord(rst) + 1 == 123:
                        rst = 'a'
                    else:
                        rst = chr(ord(rst) + 1)

            if j + 1 == index:
                result.append(rst)

    cnt = ''.join(result)
    return cnt


print(solution("x", "az", 5))