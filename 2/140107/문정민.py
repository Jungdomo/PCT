import math

def solution(k, d):
    rst = 0
    for i in range(d+1):
        i *= k
        if i <= d:
            rst += math.floor(math.sqrt(d**2 - i**2) / k) + 1

    return rst

print(solution(1, 5))