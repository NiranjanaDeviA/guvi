aa,bb=map(int,input().split())
a=aa
b=bb
while(bb):
    aa,bb=bb,aa%bb
c=(a*b)//aa
print(c)
