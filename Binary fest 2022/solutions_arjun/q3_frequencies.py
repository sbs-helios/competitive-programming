N=int(input())
S=input()
d=[]
for i in range(N):
    d.append((S.count(S[i]),S[i]))
d.sort()   
final=""  
for i in d:
    final+=i[1]
print(final)
