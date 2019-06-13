start,end=map(int,input().split()) 
for num in range(start+1, end - 1):
  if num % 2 == 0:
    print(num, end = " ") 
