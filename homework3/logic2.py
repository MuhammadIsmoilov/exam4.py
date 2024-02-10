n = int(input())
sum=0
i=0
while n>0:
    sum = sum + n%10*pow(2,i)
    i = i+1
    n//=10

print(sum)