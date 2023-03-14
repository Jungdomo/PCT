def solution(ingredient):

    i = 0
    rst = 0

    while len(ingredient)-2 >= i:
        if ingredient[i:i+4] == [1,2,3,1]:
            del (ingredient[i:i+4])
            i = i - 3
            rst += 1
        else:
            i += 1

    return rst

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]	))