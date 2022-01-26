import functools

def custom_comp(x, y):
    if int(str(x)+str(y)) > int(str(y)+str(x)):
        return -1
    return 1

for i in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort(key=functools.cmp_to_key(custom_comp))

    ans = ""

    for el in li:
        ans += str(el)

    print(ans)
