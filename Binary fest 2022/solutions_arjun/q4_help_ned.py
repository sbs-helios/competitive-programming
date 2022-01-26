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
