def solution(targets):
    targets = sorted(targets, key = lambda x : [x[1], x[0]])
    rst = 0

    n = 0
    for i in targets:
        if i[0] >= n:
            rst += 1
            n = i[1]

    return rst




print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))