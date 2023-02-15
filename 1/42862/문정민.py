def solution(n, lost, reserve):

    lost.sort()
    reserve.sort()

    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    for j in reserve:
        if j - 1 in lost:
            lost.remove(j - 1)
        elif j + 1 in lost:
            lost.remove(j + 1)

    return n - len(lost)

print(solution(5, [2,4], [1,3,5]))