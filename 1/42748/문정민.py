def solution(array, commands):
    rst = []
    for i in commands:
        cnt = array[i[0]-1:i[1]]
        cnt.sort()
        rst.append(cnt[i[2]-1])

    return rst

print(solution( [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	 ))