import math
def solution(progresses, speeds):

    rst = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(progresses))]

    cnt = rst.pop(0)
    check = 1
    result = []

    while rst:
        a = rst.pop(0)
        if cnt < a:
            cnt = a
            result.append(check)
            check = 1
        else:
            check += 1

    result.append(check)

    return result


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))