start,end=map(int,input().split())
for val in range(start+1, end):
  if val > 1:
    for n in range(2, val):
      if (val % n) == 0:
        break
    else:
      print(val,end=" ") 
