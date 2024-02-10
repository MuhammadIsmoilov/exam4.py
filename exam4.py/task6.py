def func(a, b):
    print("Name:", a, "salary:", b)
    if b == 0:
            return func(a, 9000)
a=input()
b=int(input())
print(func(a, b))