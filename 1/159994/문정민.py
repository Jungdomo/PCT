def solution(cards1, cards2, goal):
    for i in goal[:]:
        if cards1 and i == cards1[0]:
            cards1.remove(i)
            goal.remove(i)
        elif cards2 and i == cards2[0]:
            cards2.remove(i)
            goal.remove(i)
        else:
            break

    if goal:
        return "No"

    return "Yes"

print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))