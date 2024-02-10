list1 = input().split()
list2 = input().split()
for i in list1:
    if i in list2:
     print('True')  
     break
else:
 print('False')            