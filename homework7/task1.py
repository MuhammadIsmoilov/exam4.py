a = input().split()
max = -99999
cnt = 0
for i in range(1,len(a)):
    if int(a[i]) > max:
        max = int(a[i])
        cnt = i

print(max,cnt)


