def solution(answers):
    people = [[1, 2, 3, 4, 5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    result = [0] * len(people)
    for i, j in enumerate(answers):
        for k, l in enumerate(people):
            if j == l[i % len(l)]:
                result[k] += 1
    return [k + 1 for k, l in enumerate(result) if l == max(result)]