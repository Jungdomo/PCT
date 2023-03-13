def solution(food):
    rst = []
    for dex, i in enumerate(food[1:]):
        for j in range(i//2):
            rst.append(dex+1)

    result = rst.copy()
    result.sort(reverse=True)

    return ''.join(str(i) for i in rst + [0] + result)


print(solution([1, 3, 4, 6]))