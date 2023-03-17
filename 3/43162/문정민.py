from collections import deque

def solution(n, computers):
    answer = 0
    visit = [0] * n
    Q = deque()

    for i in range(n):
        if visit[i]: continue
        Q.append(i)
        answer += 1
        visit[i] = 1
        while Q:
            x = Q.popleft()
            for j in range(n):
                if not computers[x][j]: continue
                if visit[j]: continue
                Q.append(j)
                visit[j] = 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))