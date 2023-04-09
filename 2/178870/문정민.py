from collections import deque
def solution(sequence, k):

    rst = deque()

    hap = 0
    end = 0

    for i in range(len(sequence)):

        while hap < k and end < len(sequence):
            hap += sequence[end]
            end += 1

        print(hap, end)

        if hap == k:
            rst.append([i, end-1, end-1-i])

        hap -= sequence[i]

    rst = sorted(rst, key = lambda x : x[2])
    return rst[0][:2]
print(solution([1, 1, 1, 2, 3, 4, 5], 5))