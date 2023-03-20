def solution(elements):
    result = set()

    lens = len(elements)
    elements = elements * 2

    for i in range(lens):
        for j in range(lens):
            result.add(sum(elements[j:j + i + 1]))

    return len(result)

print(solution([7,9,1,1,4]))