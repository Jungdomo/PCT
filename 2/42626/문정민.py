import heapq
def solution(scoville, K):
    heap = []
    scoville.sort()

    for i in scoville:
        heapq.heappush(heap, i)

    if min(heap) >= K:
        return 0

    check = 0
    while heap[0] <= K:
        cnt = heapq.heappop(heap)
        cn = heapq.heappop(heap)

        heapq.heappush(heap, cnt + (cn * 2))

        check += 1

        if heap[0] >= K:
            return check
        if len(heap) == 1:
            return -1

print(solution([1, 2, 3, 9, 10, 12], 7))