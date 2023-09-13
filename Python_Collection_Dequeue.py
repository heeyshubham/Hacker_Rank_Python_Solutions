# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n=int(input())
for i in range (n):
    lines=input().split()
    if(lines[0]=="append"):
        d.append(int(lines[-1]))
    elif(lines[0]=="appendleft"):
        d.appendleft(int(lines[-1]))
    elif(lines[0]=="pop"):
        d.pop()
    elif(lines[0]=="popleft"):
        d.popleft()
length=len(d)
for i in range(length):
    print(d[i], end= " ")
