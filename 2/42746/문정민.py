def solution(numbers):

    numbers = sorted(numbers, reverse=True, key = lambda x : str(x) * 3)

    numbers = ''.join(str(s) for s in numbers)

    return "0" if numbers[0] == "0" else numbers

print(solution([3, 30, 34, 5, 9]))