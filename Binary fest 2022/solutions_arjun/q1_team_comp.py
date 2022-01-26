N=int(input())
count=0
for _ in range(N):
      L=list(map(int,input().split()))
      if sum(L)>=2:
            count+=1
print(count)
