def solution(sizes):
    answer = 0
    array1 = []
    array2 = []
    for x in range(len(sizes)):
        array1.append(max(sizes[x]))
        array2.append(min(sizes[x]))
    answer = max(array1) * max(array2)
    return answer
