def solution(n):
    answer = 0
    if n>0:
        for i in range(1, n+1):
            if n % i == 0:
                answer += i
    else:
        return 0
    return answer

solution(12)