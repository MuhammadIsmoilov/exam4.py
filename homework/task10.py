first =  int(input())
second = int(input())
third =  int(input())
if first == second and second == third and third == first:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first != second and second != third and third != first:
    print(0 )    