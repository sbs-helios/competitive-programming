answer = 0

for i in range(int(input())):
    li = list(map(int, input().split()))

    if sum(li) >= 2:
        answer += 1

print(answer)
