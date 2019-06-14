n=int(input())
x=0
y=1
for i in range(1,n+1):
  if(i<=1):
    a=i
  else:
    a=x+y
    x=y
    y=a
  print(a,end=" ")
