from math import gcd
def solution(arr):
    answer = arr[0]
    for ar in arr:
        answer = answer * ar // gcd(ar, answer)
    return answer