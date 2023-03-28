def solution(n, arr1, arr2):

    cnt = [[" " for i in range(n)] for i in range(n)]
    cnt2 = []

    rst = []
    rst2 = []
    for i in arr1:
        ss = bin(i).split("b")[1]
        if len(ss) < n:
            ss = "0"*(n-len(ss)) + ss
        rst.append(ss)  

    for i in arr2:
        ss = bin(i).split("b")[1]
        if len(ss) < n:
            ss = "0" * (n - len(ss)) + ss
        rst2.append(ss)

    for i in range(n):
        for j in range(n):
            if rst[i][j] == "1" or rst2[i][j] == "1":
                cnt[i][j] = "#"

    for i in cnt:
        cnt2.append(''.join(i))

    return cnt2


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))