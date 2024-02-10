list1 = input().split()
number = int(input())
cnt = 1
for i in list1:
    if int(i)>=number:
        cnt+=1
print(cnt)         