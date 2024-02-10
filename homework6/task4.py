n = input().split()
number =len(n)
i = 1 
while i < number:
  if n[i] > n[i-1]:
      print(n[i],end=" ")
  i+=1