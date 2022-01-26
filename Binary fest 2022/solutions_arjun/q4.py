'''
N=int(input())
A=[]
for i in range(N):
    l=list(map(int,input().split()))
    A.append(l)

all=[]

for i in range(N-2):
    for j in range(N-2):
        h=A[i][j:j+3]+[A[i+1][j+1]]+A[i+2][j:j+3]
        print(h,sum(h))
        all.append(sum(h))

print(max(all))
'''

T = int(input())
for i in range(T):
    N = int(input())
    L = input()
    L = L.split()
    L = [int(i) for i in L]
    L.sort()
    L.reverse()
    L = [str(i) for i in L]
    #print(L)
    while True:
        flag = 0
        for i in range(N):
            if i == N-1:
                break
            if L[i][0] < L[i+1][0]:
                L[i], L[i+1] = L[i+1], L[i]
                flag = 1                
        if flag == 0:
            break
    print("".join(L))

