# list1 = input().split()                   task1
# sum = 0
# for i in list1:
#     sum +=int(i) 
# print(sum)




# list1 = input().split()            task2
# sum = 1
# for i in list1:
#     sum *= int(i)
# print(sum)


# list1 = input().split()         task3
# maxx = -9999
# for i in list1:
#     if int(i) > maxx:
#         maxx = int(i)
# print(maxx)




# def list_of_min_numbers(minn = 9999):
#         list1 = input().split()          task4
#         for i in list1:
#             if int(i) < minn:
#                   minn = int(i)
#         return minn

# print(list_of_min_numbers())       




# words = input().split()                task5
# ctr = 0
# for i in words:
#   if len(i) > 1 and i[0] == i[-1]:
#       ctr += 1
# print(ctr)                                





# def last(n):
#     return n[-1]                        task6
# def sort_list_last(tuples):
#     return sorted(tuples, key=last)
# print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


  
# m = input().split()
# b = set(m)
# print(m)            task7




# element = input().split()
# if len(element) == 0:            task8
#         print('is empty')
# else:
#         print('is not empty')
     
   

# list1 = input().split()        task9
# new_list = list(list1)
# print(new_list) 




# words = str.split(" ")
# new_list = []                  task 10 -> ?
# n = input()
# for i in words:
#     if len(i) > int(n):
#         new_list.append(i)
# print(new_list)         



# list1 = input().split()
# list2 = input().split()
# for i in list1:
#     for j in list2:
#         if i == j:
#             print('True')
#         else:
#          print('False')




# list1 = input().split()
# for i in list1:
#     if int(i) % 2 == 0:
#         list1.remove(i)     
# print(list1)        






# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# set1 = set(list1)
# set2 = set(list2)

# difference = list(set1.symmetric_difference(set2))

# print("Difference between the two lists:", difference)





# list = input().split()
# for i in enumerate(list):
#     print(i ,  end=" ")



# list1 = input().split()
# list2 = int(input())
# for i in range(len(list1)):
#      if int(list1[i]) == list2:
#        print(i)
# else:
#     print('Your number is not here')




# list1 = input().split()
# list2 = input().split()
# list3 = list1 + list2
# print(list3)



# m = input().split()
# maxx = -9999
# for i in m:
#     if int(i) > int(maxx):
#         maxx = i
#         m.remove(maxx)
# for i in m:
#     if i > maxx:
#             maxx = i
# print(maxx)