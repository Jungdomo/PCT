def solution(keymap, targets):
    from collections import defaultdict

    key = defaultdict(lambda: [])
    result = []

    for i in keymap:
        for ind, val in enumerate(i):
            key[val].append(ind + 1)

    for i in targets:
        cnt = 0
        for j in i:
            if key.get(j) is None:
                result.append(-1)
                break
            else:
                cnt += min(key[j])

        if key.get(j) is not None:
            result.append(cnt)

    return result

print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))