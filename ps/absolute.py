def solution(a, s):
    answer = 0
    for i in range(len(a)):
        if s[i] == False:
            a[i] = -a[i]
        answer += a[i]
    return answer
