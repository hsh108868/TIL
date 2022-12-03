def solution(s):
    answer = -1
    stack = [s[0]]

    if len(s) % 2 == 1:
        return 0
    if len(s) == 2:
        return 1 if s[0] == s[1] else 0

    for i in s[1:]:
        if len(stack) and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return 0 if len(stack) else 1
