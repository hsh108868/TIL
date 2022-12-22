from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse =True))
    while len(people) > 1:
        if people[0] + people[-1] > limit: # 배열 -1은 마지막 값을 가져온다.
            answer += 1
            people.popleft()
        else: 
            answer += 1
            people.popleft()
            people.pop()
    if people:
        answer += 1
    return answer
