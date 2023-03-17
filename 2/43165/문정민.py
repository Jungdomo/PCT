def solution(numbers, target):
    dfs(numbers, 0, 0, target)
    return count

count = 0

def dfs(numbers, s, k, tar):
    global count
    if len(numbers) == k:
        if s == tar: count += 1
        return

    dfs(numbers, eval(str(s)+"+"+str(numbers[k])), k+1, tar)
    dfs(numbers, eval(str(s)+"-"+str(numbers[k])), k+1, tar)