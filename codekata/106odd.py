x,y=map(int,input().split())
z=list(map(int,input().split()))
if z[y]%2!=0:
    print(z[y])
else:
    print(z[y-1])
