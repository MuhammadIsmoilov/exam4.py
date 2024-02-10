# list1 = input().split()
# list2 = input().split()
# list3 = ''.join(list1[0] + " " + list2[0])             misoli 1
# list4 = ''.join(list1[0] + " " + list2[1])
# list5 = ''.join(list1[1] + " " + list2[0])
# list6 = ''.join(list1[1] + " " + list2[1])
# main_list = []
# main_list.append(list3)
# main_list.append(list4)
# main_list.append(list5)
# main_list.append(list6)
# print(main_list)





# list1 = ['gov','','har','asp', '']
# i = ''
# while i in list1:            misoli 2
#     list1.remove(i)        
# print(list1)



# list1 = [10,20, [300,400,[50000,6000],500],30,40]
# list2 = list1[2][2]                               misoli 3
# list2.append(7000)
# print(list1)





# list1 = ['a','b',['c',['d','e',['f','g'],'k'],'l'],'m','n']
# list2 = list1[2][1][2]
# list2.append('h')
# list2.append('i')                 misoli 4
# list2.append('j')
# print(list1)




# list1 = [5, 20, 15, 20, 25, 50, 20]       misoli 5
# n = int(input())
# i = n
# while n in list1:
#     list1.remove(n)
# print(list1)




# my_dict1 = {
#     'Ten': 10,
#     'Twenty':20,
#     'Thirty':30}
    
# my_dict2 = {
#     'Thirty': 30,                 misoli 6
#     'Fourty':40,
#     'Fifty':50}

# my_dict1.update(my_dict2)
# print(my_dict1)



# dict1 = {}
# dict2 = {}
# i = 0
# while i < 3:
#     key_input = (input('Enter a key -> '))
#     value_input = (input('Enter a value ->'))
#     dict1[key_input] = value_input
#     i += 1
# j = 0
# while j < 3:
#     key_input = (input('Enter a key -> '))
#     value_input = (input('Enter a value ->'))
#     dict2[key_input] = value_input
#     j += 1
# print(dict1)
# print(dict2)


# sampleDict = {          misoli 7
# "class": {
#     "student": {
#         "name": "Mike" ,
#         "marks": {
#             "physics": 70,
#             "history": 80
#           }
#         }
#     }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])




# sample_dict = {
# "name": "Kelly",
# "age": 25,
# "salary": 8000,            misoli 8
# "city": "New york"}
# del sample_dict['name']
# del sample_dict['salary']
# print(sample_dict)



# enter_name = input().split()
# dict = {'designation': 'Developer','Salary':8000}
# empty_dict = {}
# for i in enter_name:                 misoli 9
#     empty_dict[i]=dict
# print(empty_dict)



# dict1 = {'a':100, 'b':200, 'c':300}          misoli10
# n = int(input())
# if n  in dict1.values():
#     print('present')
# else:
#     print('false')
