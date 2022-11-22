def solution(s):
    answer = True
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif len(stack) and i == ")":  # stack에 (가 있고 i가 )면
            stack.pop()
# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return len(stack) == 0
