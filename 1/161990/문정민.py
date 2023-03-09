def solution(wallpaper):
    x = []
    y = []
    result = []

    for index, i in enumerate(wallpaper):
        for dex, v in enumerate(i):
            if v == "#":
                y.append(index)
                x.append(dex)

    result.append(min(y))
    result.append(min(x))
    result.append(max(y)+1)
    result.append(max(x)+1)

    return result

print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))