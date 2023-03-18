from collections import deque
def solution(maps):
    visit = [[0 for i in maps[0]] for i in range(len(maps))]
    visited = [[0 for i in maps[0]] for i in range(len(maps))]
    dx, dy = [0,1,0,-1],[1,0,-1,0]
    q = deque()
    Q = deque()
    check = 0

    for i in range(len(maps)):
        for dex, j in enumerate(maps[i]):
            if j == "S":
                q.append([i, dex])
                visit[i][dex] = 1

    while q and not check:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
            if maps[nx][ny] == "X" or visit[nx][ny]: continue
            q.append([nx, ny])
            visit[nx][ny] = visit[x][y] + 1
            if maps[nx][ny] == "L":
                Q.append([nx, ny])
                check = visit[nx][ny]-1
                visited[nx][ny] = 1

    if not Q:
        return -1

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
            if maps[nx][ny] == "X" or visited[nx][ny]: continue
            Q.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1
            if maps[nx][ny] == "E": return visited[nx][ny]-1 + check

    return -1

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))