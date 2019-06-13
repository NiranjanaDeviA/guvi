x=int(input())
y=0
t=x
while t>0:
  digit=t%10
  y+=digit**3
  t//=10
if x==y:
    print("yes")
else:
    print("no")
