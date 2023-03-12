def solution(k, m, score):
    a = 0
    rst = 0
    scores = [k if i > k else i for i in score]
    scores.sort(reverse=True)

    for i in scores:
        if len(scores[a:a+m]) != m:
            break
        rst += min(scores[a:a+m]) * len(scores[a:a+m])
        a += m

    return rst

print(solution(3, 4, [1,2,3,1,2,3,4]))