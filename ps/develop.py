def solution(p, s):
    answer = []
    while p:
        result = 0
        for i in range(len(p)):
            p[i] += s[i]
        while p and p[0] >= 100:
            p.pop(0)
            s.pop(0)
            result += 1
        if result > 0:
            answer.append(result)
    return answer
