import heapq
import math
def solution(jobs):
    cnt, i = 0, 0
    start, now = -1, 0
    heap = []

    while i < len(jobs):

        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        if heap:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            cnt += now - cur[1]
            i += 1

        else:
            now += 1

    return math.floor(cnt//len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))
