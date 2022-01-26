N,K=map(int,input().split())
L=list(map(int,input().split()))

areas=[]
for i in range(N-K+1):
      smol=L[i]
      for j in range(i,i+K):
            if L[j]<smol:
                  smol=L[j]
      areas.append(smol*K)

print(max(areas))
