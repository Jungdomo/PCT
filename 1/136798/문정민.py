from collections import deque
def solution(number, limit, power):
    kg = deque()

    for i in range(1, number+1):
        gcd = get_num(i)

        if limit < gcd:
            kg.append(power)
        else:
            kg.append(gcd)

    return sum(kg)

def get_num(n):
    cnt = 0

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i == n//i:
                cnt += 1
            else:
                cnt += 2

    return cnt

print(solution(5, 3, 2))