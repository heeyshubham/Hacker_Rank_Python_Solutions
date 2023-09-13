
from collections import *
n= int(input())
d= OrderedDict()
for i in range (n):
    word=input()
    if(d.get(word)):
        d[word] +=1
    else:
        d[word] =1
print(len(d))
for i in d.keys():
    print(d[i], end=" ")
