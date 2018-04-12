
S,N = map(int, input().split())
marksheet = []
for _ in range(N):
    marksheet.append(map(float, input().split()))
for i in zip(*marksheet):
    print(sum(i)/len(i))