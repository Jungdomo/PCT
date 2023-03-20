from collections import deque
def solution(board):

    visit = [[0 for i in board[0]] for i in range(len(board))]
    q = deque()
    dx, dy = [0,0,1,-1], [1,-1,0,0]

    for d, i in enumerate(board):
        for dex, j in enumerate(i):
            if j == "R":
                q.append([d, dex, 0])

    while q:
        x, y, length = q.popleft()
        if visit[x][y]:
            continue
        if board[x][y] == "G":
            return length
        visit[x][y] = 1
        for i in range(4):
            nx, ny = x, y
            while True:
                qx, qy = nx + dx[i], ny + dy[i]
                if 0 <= qx < len(board) and 0 <= qy < len(board[0]) and board[qx][qy] != "D":
                    nx, ny = qx, qy
                    continue
                q.append([nx, ny, length + 1])
                break

    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))