for i in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    answer = 0

    for i in range(n-k+1):
        tmp_min = lst[i]

        for j in range(i+1, i+k):
            tmp_min = min(tmp_min, lst[j])

        answer = max(answer, tmp_min * k)

    print(answer)
