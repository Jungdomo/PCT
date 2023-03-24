from collections import deque
def solution(cache_size, cities):
    q = deque()
    cnt = 0

    for i in cities:
        i = i.upper()
        if not i in q:
            cnt += 5
        else:
            q.remove(i)
            cnt += 1

        q.append(i)
        if len(q) == cache_size + 1:
            q.popleft()

    return cnt

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
