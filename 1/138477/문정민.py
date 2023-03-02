def solution(k, score):
    stack = []
    rst = []

    check = 0

    for i in score:
        stack.append(i)
        stack.sort(reverse=True)
        rst.append(stack[check])
        if check < k-1:
            check += 1

    return rst

print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))