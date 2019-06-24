aa,bb=map(int,input().split())
x=aa
y=bb
while(bb):
    aa,bb=bb,aa%bb
z=(x*y)//aa
print(z)
