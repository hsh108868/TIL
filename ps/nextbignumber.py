def solution(n):
    count = n + 1

    while True:
        if bin(n).count('1') == bin(count).count('1'):
            return count
        else:
            count += 1
