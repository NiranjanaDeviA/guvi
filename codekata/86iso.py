s=list(input())
p=[]
for i in s:
    if i not in p:
        p.append(i)
if s==p:
    print("Yes")
else:
    print("no")
