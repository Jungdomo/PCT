from collections import deque
def solution(m, musicinfos):
    answer = {}
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for i in musicinfos:
        ss = deque()
        start, end, title, code = i.split(",")

        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute

        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start

        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

        check = 0
        for j in range(duration):
            ss.append(code[check])
            check += 1
            if len(code) == check:
                check = 0

        if m in ''.join(ss): answer[title] = duration

    if len(answer) == 0:
        return "(None)"

    return sorted(answer.items(), key=lambda x: x[1], reverse=True)[0][0]

print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))