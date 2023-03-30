def solution(prices):
    result = []
    for i in range(len(prices)):
        check = 0
        ch = 0
        for j in range(i, len(prices)):
            if prices[i] > prices[j]:
                ch += 1
                break
            else:
                check += 1
        if ch == 1:
            result.append(check)
        else:
            result.append(check-1)

    return result


print(solution([1, 2, 3, 2, 3]))