n=int(input())
marksheet = [[input(),float(input())] for _ in range(n)]
mark=sorted(list(set([marks for name,marks in marksheet])))[1]
res = [a for a,b in sorted(marksheet) if b== mark]
print(*res,sep="\n")