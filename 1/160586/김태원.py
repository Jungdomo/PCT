def solution(keymap, targets):
    list = {}

    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in list:
                list[key] = i + 1
            else:
                list[key] = min(list[key], i+1)

    result = []
    for target in targets:
        cnt = 0
        for key in target:
            if key not in list:
                cnt = -1
                break
            cnt += list[key]
        result.append(cnt)

    return result

print(solution(["ABACD", "BCEFD"],["ABCD","AABB"]))