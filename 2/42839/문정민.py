from itertools import permutations

def check(rst):
    if rst == 0 or rst == 1:
        return False
    for i in range(2, rst):
        if rst % i == 0:
            return False
    return True

def solution(numbers):

    result = []
    for i in range(len(numbers)):
        cnt = list(map(''.join, permutations(numbers, i + 1)))

        for p in set(cnt):
            if check(int(p)):
                result.append(int(p))

    return len(set(result))

print(solution("011"))