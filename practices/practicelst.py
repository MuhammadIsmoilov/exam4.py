# a = input().split()
# b = input().split()
# c = []
# for i in a:
#     if i in b:
#       c.append(i)
# print(c,end=" ")   
  

# a = input().split()
# b = input().split()
# c = []
# for i in a:
#     if i  not in b:
#       c.append(i)
# print(c)


# square = lambda n:n * n
# print(square(4))

# def update_id():
#     id_input = input('Choose which id you want to change?')
#     user_input = input('Choose which user you want to change?')
#     task_input = input('Choose which task you want to change?')
#     due_input = input('Choose which due date you want to change?')
#     time_input = input('Choose which time you want to change?')
#     for j in dict_list:
#         if id_input in j.values():
#              j.update({
#                 'Id': id_input,
#                 'User': user_input,
#                 'Task':task_input,
#                 'Due_date': due_input,
#                 'Time': time_input, 
#             })

# languages = ['c','cpp','java',]
# languages.append(['python','csharp'])
# print(languages)





# languages = ['c','cpp','java',]
# more_langugages = ['python','csharp']
# languages.extend(more_langugages)
# print(languages)




# n = int(input('Enter the number of elements: '))
# numbers = []
# for i in range(n + 1):
#     x = int(input())
#     numbers.append(x)
# print(numbers)




# n = int(input('Enter the number of elements: '))
# numbers = input().split()
# for i in range(0, n):
#     numbers[i] = int(numbers[i])
#     print(numbers)   





# def f(x):
#     return x**2

# a = [1,-2,3,-4,5]
# b = list(map(f, a))
# print(b)









# a = ['goofbyr', 'go eat somrthing','help']
# b = list(map(str.upper, a))
# print(b)


# a = ['goofbyr', 'go eat somrthing','help']
# b = list(map(len, a))
# print(b)



# list = [1,2,3,4,5,6]
# list2 = list[::-1]
# print(list2)







# a = ['goofbyr', 'go eat somrthing','help']
# b = list(map(lambda x:x[::-1], a))
# print(b)






# a = ['goofbyr', 'go eat somrthing','help']
# b = list(map(list, a))
# print(b)



# a = ['goodbye','go eat ','help']
# b = list(map(list, a))
# c = list(map(sorted,b))
# print(c)



# a = list(map(int,input().split()))
# print(a)



# set = {'home',23,1,2,3,3,1}
# print(set)

# def addition(a,b):
    
#     def adding():
       
#        return a + b
#     return adding() + 5
# m = addition(12,32)
# print(m)




# def summing(n,sum = 0):
#     if n == 0:
#         return sum
#     sum += n
#     return summing(n-1,sum)
# a = int(input())
# print(summing(a))






# def summing(n,sum = 0,index = 1):
#     sum += index
#     if n == index:
#         return sum

#     return summing(n,sum,index + 1)
# a = int(input())
# print(summing(a))



# a = int(input())
# b = int(input())
# for i in range(a,b,2):
#     print(i)


# a = input()
# b = len(a)
# y = b//2
# c = a[0],a[y],a[-1]
# print(f"{c}")  


# list1 = [5,[10,15[20,15[30,35],40],45],50]
# list1[1][2][2][1]
# print(list1)
    


# a = input()
# b = len(a)           misoli1
# y = b//2
# z = b//2-1
# x = b//2+1
# c = a[z],a[y],a[x]
# print(f"{c}") 


# str1 = input()
# str2 = input()          misloli2
# str3 = ''
# a = len(str1)
# b = a//2
# str3 = str1[0:b]+str2[::]+str1[d:]

# print(f"{str3}")



# str1 = input()
# str2 = input()
# a = len(str1)        misoli 3
# b = a//2
# c = len(str2)
# d = c//2
# str3 = str1[0]+str2[0]+str1[b]+str2[d]+str1[-1]+str2[-1]
# print(f"{str3}")



# str1 = input()
# str3 = ''
# str4 = ''
# str5 = ''                      misoli4
# for i in str1:
#     if (i.islower()):
#         str3 += i
#     elif (i.isupper()):
#         str4 += i
# str5 = str3 + str4
# print(str5)


# list = input()
# n = list.isalpha()
# cnt = 0
# cnt2 = 0  
# cnt3 = 0                     misoli 5
# for i in list:
#     if (i.isalpha()) == True:
#         cnt += 1
#     elif (i.isdigit()) == True:
#         cnt2 += 1  
#     else:
#         cnt3 += 1      
# print(f"words {cnt}")
# print(f"numbers {cnt2}")
# print(f"symbols{cnt3}") 





# str1 = input().lower()
# str2 = input().lower()
# if str1 in str2:          misoli6
#     print('True')
# else:
#     print('False') 







# n = int(input())
# for i in range(1,n+1):         misoli7
#    for j in range((n+1)-i):        
#      print(i, end=" ")
#    print() 




# def addition(a,b):           misoli8
                              
#     def adding():
       
#        return a + b
#     return adding() + 'developer'
# m = addition('emma','kelly')
# print(m)



# def rectangle(n,i = 0):
#        print(i,end=" ")
#        if i == n:
#               return 0
#        return rectangle(n,i+1)
# n = int(input())
# res = rectangle(n)
# print(res)                

                                            
# def rectangle(n,i = 1):                           
       
#        if i == n:
#               print(n)
#               return 0
#        def inner(num = n+1-i, j = 0):
#               print(i,end=" ")
#               if num == j:
#                      return 0 
#               return inner(num, j+1)
#        inner()
#        print()       
#        return rectangle(n,i+1)
# n = int(input())
# res = rectangle(n)
# print(res) 





# list1 = input().split()
# list2 = input().split()
# for i in range(len(list1)):
#     print(f"{list1[i]} {list2[-1-i]}")




# list1 = input().split()
# list2 = input().split()
# my_dict = {}
# for i in list1:
#     for j in list2:
#        my_dict[i] = j
# print(my_dict)





  