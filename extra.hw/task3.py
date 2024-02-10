m = input()
t = input()
cnt = 0
for i in m:
    if i in t:
        cnt += 1
if cnt > 0:
    print('True')
else:
    print('False')            