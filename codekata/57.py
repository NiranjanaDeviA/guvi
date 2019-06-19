n,k=map(int,input().split())
li=list(map(int,input().split()))
count=0
for i in li:
  if(i==k):
    count=count+1
print(count)
