a = int(input())
b = int(input())
i = 1
while i <= b:
    if i*i >= a and i*i <=b:
        print(i*i)
        i = i+1