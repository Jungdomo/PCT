def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    ones = 0
    twos = 0
    threes = 0

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in answers:
        if one[ones] == i:
            cnt1 += 1
        if two[twos] == i:
            cnt2 += 1
        if three[threes] == i:
            cnt3 += 1

        ones += 1
        twos += 1
        threes += 1

        if len(one) == ones:
            ones = 0
        if len(two) == twos:
            twos = 0
        if len(three) == threes:
            threes = 0

    rst = []

    rst.append(cnt1)
    rst.append(cnt2)
    rst.append(cnt3)

    cnt = 1
    result = []
    for i in rst:
        if i == max(rst):
            result.append(cnt)
        cnt += 1

    return result



print(solution([1,3,2,4,2]	))