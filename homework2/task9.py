x = int(input())
d = int(input())
i = x
s = 0
cnt=0
while i > 0:
    s = i % 10
    if s == d:
     cnt=cnt+1
    i=int(i/10)
print(cnt)