element = input().split()
minn = 99999
for i in element:
    if int(i) > 0 and int(i) < int(minn):
        minn=i   
print(minn)