def solution(numbers):
    answer = [-1 for _ in numbers]
    s = []
    for i,n in enumerate(numbers):
        if s and n > s[-1][1]:
            while s and n > s[-1][1]:
                index, _ = s.pop()
                answer[index] = n
        s.append((i,n))

    return answer

print(solution([2, 3, 3, 5]))