n = int(input())
grid = []
answer = 0

for i in range(n):
    li = list(map(int, input().split()))
    grid.append(li)

for i in range(n-2):
    for j in range(n-2):
         answer = max(answer, grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2])

print(answer)
