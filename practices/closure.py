# def my_printer():
#     msg = 'hi there'
#     def printer():
#         print(msg)
#     return printer
# a = my_printer()
# a()
# a()
# a()
# a()



# def power(n):
#     def inner(m):
#         print(n**m)
#     return inner
# power1 = power(12)
# power1(2)    



# def power(n):
#     def inner(index = 1):
#         if index == 10:
#             return 0
#         print(f"{n} * {index} = {n * index}")
#         return inner(index + 1)
#     return inner
# power1 = power(12)
# power1(2)




# def power(n):
#     def inner(index = 1,m = 10):
#         if index == m:
#             return 0
#         print(f"{n} * {index} = {n * index}")
#         return inner(index + 1,m)
#     return inner
# power1 = power(12)
# power1(2,23)





# def power(n):
#     def inner(index = 1,m = 10):
#         if index == m:
#             return 0
#         print(f"{n} * {index} = {n * index}")
#         return inner(index + 1,m)
#     return inner
# power1 = power(int(input()))
# a = int(input())
# b = int(input())
# power1(a, b)




# square = lambda n:n * n
# print(square(4))


# message = lambda:print('hello')
# message()

# (lambda x,y :print(f"{x} * {y} = {x * y}"))(12,23)


numbers = input().split()
conver_to_int = lambda x:int(x)
num = map(conver_to_int, numbers)
# num = map(conver_to_int, numbers)
print(list(num))
print(*numbers)
# print(conver_to_int('12'))