a=int(input())
l=list(map(int,input().split()))
if a==len(l):
  s=sum(l)
  b=s//a
print(b)
