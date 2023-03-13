def solution(nums):
    key = {}
    for i in nums:
        if not key.get(i):
            key[i] = 1
        else:
            key[i] += 1

    if len(key) <= len(nums)//2:
        return len(key)
    return len(nums)//2

print(solution([3,1,2,3]))