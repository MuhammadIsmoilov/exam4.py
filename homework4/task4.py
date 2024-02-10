a = int(input())
b = int(input())
for i in range(a,b+1):
    cnt = 0
    for j in range(2,a):
        if i % j==0:
            cnt+=1
    if(cnt==0):
     print(i, end=" ")        