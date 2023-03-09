def solution(keymap, targets):
    from collections import defaultdict, deque

    table, answer = defaultdict(lambda: deque()), []

    for i in keymap:
        for ind, val in enumerate(i):
            table[val].append(ind + 1)

    for i in targets:
        cnt = 0
        for j in i:
            if table.get(j) is None:
                answer.append(-1)
                break
            else:
                cnt += min(table[j])
                
        if table.get(j) is not None:
            answer.append(cnt)

    return answer
