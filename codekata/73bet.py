a=int(input())
x,y=map(int,input().split())
for i in range(x+1,y):
  if(a==i):
    print("yes")
    break
else:
  print("no")  
