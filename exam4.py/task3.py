def counter(name = 'Emma is good developer. Emma is a writer',cnt = 1):
    for i  in name:
        if (i.isalpha()):
            cnt+=1
            return cnt
name = input()
print(counter(name))