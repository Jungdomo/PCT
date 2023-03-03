from math import gcd

def solution(arrayA, arrayB):
    a = arrayA.copy()
    b = arrayB.copy()
    while len(arrayA) != 1: arrayA.append(gcd(arrayA.pop(), arrayA.pop()))
    while len(arrayB) != 1: arrayB.append(gcd(arrayB.pop(), arrayB.pop()))

    for i in range(len(a)):
        if a[i] % arrayB[0] == 0:
            arrayB[0] = 1
        if b[i] % arrayA[0] == 0:
            arrayA[0] = 1

    if arrayA[0] == arrayB[0] == 1:
        return 0
    else:
        max(arrayA[0], arrayB[0])

print(solution([10, 17], [5, 20]))