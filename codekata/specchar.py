import re
t=input()
c=len(t)-len(re.findall('[\w]',t))
print(c)

