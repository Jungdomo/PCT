def solution(citations):
    citations.sort(reverse=True)
    rst = 0
    for i in enumerate(citations):
        if i[1] >= i[0]+1:
            rst += 1

    return rst

print(solution([3, 0, 6, 1, 5]))