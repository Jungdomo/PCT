from collections import deque

def solution(people, limit):
    result = 0
    people.sort()
    q = deque(people)
    
    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.popleft()
        result += 1
        q.pop()

    if q:
        result += 1
    return result

print(solution([70, 50, 60, 50], 100))

## list 여부 체크할때는 len(list) == 0 이런식이 아니라 그냥 if list 이런식으로
## deque 활용 (스택, 큐를 동시에 활용이 가능함)
## 코드는 하나씩 차례대로 적기
## while 문을 조건달고 if문으로 예외처리하면서 공통로직은 최대한 while문에서 처리하기
## ㅈㄴ어렵네 진짜