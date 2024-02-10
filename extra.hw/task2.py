n = input().split()
minn = 99999
for i in n:
    if int(i) < int(minn):
        minn = i
n.remove(minn)
for i in n:
     if i < minn:
         minn = i
print(minn)                        