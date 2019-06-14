def isPowerOfTwo(s):
  return(s and (not(s & (s-1))))
n=int(input())
if(isPowerOfTwo(n)):
  print("yes")
else:
  print("no")
