a = int(input())
cnt = 0
i = a
while i>0:
    cnt=cnt+i%10
    i = int(i/10)
print(cnt)

