def solution(genres, plays):

    rst = {}
    result = []

    for i in range(len(genres)):
        if not rst.get(plays[i]):
            rst[plays[i]] = []
            rst[plays[i]].append(i)
        else:
            rst[plays[i]].append(i)

    key = {}

    for i in range(len(genres)):
        if not key.get(genres[i]):
            key[genres[i]] = []
            key[genres[i]].append(plays[i])
        else:
            key[genres[i]].append(plays[i])

    cnt = sorted([i for i in key.values()], key = lambda x : sum(x), reverse=True)

    for i in cnt:
        check = 0
        i.sort(reverse=True)
        for j in i:
            if check >= 2:
                break
            result.append(rst.get(j)[0])
            rst.get(j).pop(0)
            check += 1

    return result

print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500]))