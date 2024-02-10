def sum_number(n, m, sum = 0):
  s = m
  for i in range(n):
    sum += int(m)
    m = m * 10 + s
  return sum
num1 = int(input())
num2 = int(input())
print(sum_number(5, 2))