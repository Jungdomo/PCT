def solution(survey, choices):
    key = {}
    an = [3,2,1,0,1,2,3]
    am = ['R','T','C','F','J','M','A','N']
    rst = []
    for dex, i in enumerate(survey):
        if choices[dex] > 4:
            a = ''.join(i[1])
            if not key.get(a):
                key[a] = an[choices[dex]-1]
            else:
                key[a] += an[choices[dex] - 1]
        elif choices[dex] < 4:
            b = ''.join(i[0])
            if not key.get(b):
                key[b] = an[choices[dex]-1]
            else:
                key[b] += an[choices[dex]-1]
        else:
            continue

    v = 0
    for i in am:
        if not key.get(i):
            key[i] = 0
        v += 1
        if v % 2 == 0:
            if key.get(am[v-2]) > key.get(am[v-1]):
                rst.append(am[v-2])
            elif key.get(am[v-1]) > key.get(am[v-2]):
                rst.append(am[v-1])
            else:
                rst.append(am[v-2])

    return ''.join(rst)
print(solution(["TR", "RT", "TR"], [7, 1, 3]))