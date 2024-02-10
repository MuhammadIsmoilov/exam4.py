x = int(input())
cnt = 1
i = 1
while i <= x:
     if i == x: 
        cnt += 1
else: cnt = 0
i *= 2
if cnt > 0:
     print("YES")
else:
     print("NO")