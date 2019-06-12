a=int(input())
x=a
temp=0
while x!=0:
  temp=(temp*10)+(x%10)
  x=x//10
if(a==temp):
  print("yes")
else:
  print("no")
