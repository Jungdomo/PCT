def solution(players, callings):
    p_index = {p: i for i, p in enumerate(players)}
    i_player = {i: p for i, p in enumerate(players)}

    for i in callings:
        current = p_index[i]
        back = current-1
        current_v = i
        back_v = i_player[back]

        p_index[current_v] = back
        p_index[back_v] = current

        i_player[back] = current_v
        i_player[current] = back_v

    return list(i_player.values())

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))