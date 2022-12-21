def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] == "":
            continue
        s[i] = s[i][0].upper() + s[i][1:].lower()
        if s[i][0] == ' ':
            s[i] = s[i][1].upper() + s[i][2:].lower()
    return ' '.join(s)
