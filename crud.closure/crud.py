dict_list = []

def create():
    def create_dict():
        for i in dict_list:
            for key, value in i.items():
                return 

    create_id = {
        'Id': input('Your id please:'),
        'User': input('Name:'),
        'Task': input('Task:'),
        'Due_date': input('Due_date:'),
        'Time': input('Time:')
    }

    dict_list.append(create_id)

    return create_dict

n = create()
print(n())


# while True:
#       print("""
#               c -> create
#               e -> exit""")
#       m = input('->')
#       match m:
#           case 'c':
#               create()





                