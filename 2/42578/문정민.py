def solution(clothes):

    key = {}
    cnt = 1

    for i in clothes:
        if not key.get(i[1]):
            key[i[1]] = 1
        elif key.get(i[1]):
            key[i[1]] += 1

    for i in key.values():
        cnt *= i+1

    return cnt-1

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))