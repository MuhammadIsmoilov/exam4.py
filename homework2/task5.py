x = int(input())
y = int(input())
cnt = 1
while x < y:
    x += x * 0.1
    cnt += 1
print(cnt)