from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    visit = [[0 for i in range(M)] for i in range(N)]
    Q = deque()
    Q.append([0,0])
    visit[0][0] = 1
    dx, dy = [1,0,-1,0], [0,1,0,-1]

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if maps[nx][ny] == 0 or visit[nx][ny]: continue
            Q.append([nx, ny])
            visit[nx][ny] = visit[x][y] + 1


    return visit[-1][-1] if visit[-1][-1] else -1