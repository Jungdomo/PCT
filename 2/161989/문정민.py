def solution(n, m, section):
    start = 0
    answer = 0

    for i in section:
        if start < i:
            start = i+m-1
            answer += 1

    return answer

print(solution(8, 4, [2, 3, 6]))