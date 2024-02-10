def delete_index(a,n):
    ind = ''
    for i in len(a):
        if n < len(a):
            ind += a[n]
            n+=1
    return ind
name = input()
n = int(input())
print(delete_index(name,n))


