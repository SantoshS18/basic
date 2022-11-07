a=int(input())
l=list(map(int,input().strip().split()))[:a]
print(max(l))
print(min(l))
n=sum(l)/2
print(n)
