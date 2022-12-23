user_input = int(input())
answer = 2
if user_input == 1:
    print("Yes")
elif user_input >= 2:
    while user_input > answer:
        answer *= 2
    if user_input == answer:
        print("Yes")
    else:
        print("No")
