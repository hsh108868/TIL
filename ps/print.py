from collections import deque


def solution(p, l):
    answer = 0
    q = deque([(v, i) for i, v in enumerate(p)])

    while len(q):
        cur = q.popleft()
        if q and max(q)[0] > cur[0]:
            q.append(cur)
        else:
            answer += 1
            if cur[1] == l:
                break
    return answer
