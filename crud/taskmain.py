dict_list = []
def creat():
    my_dict = {
        'Id':input('Your id plase:'),
        'User' : input('Enter your name please:'),
        'Task' : input('Write what will you do:'),
        'Due_date' : input('Write your due date please:'),
        'Time': input('Write please in what time will you do this:') }
    dict_list .append(my_dict)


def get_task():
    for i in dict_list:
        for key,value in i.items():
           print(value,end=" ")
        print()
def update_id():
    id_input = input("which id you want to change ?")
    for i in dict_list:
      if id_input in i.values():
        user_input = input ("Change  user to : ")
        task_input = input ("Change task to : ")
        due_date_input = input ("Change  due date to ")
        time_input = input ("Change  time to ")
        id_input.update({
                     "id":id_input,
                     "user":user_input,
                     "task":task_input,
                     "due_date":due_date_input,
                     "time": time_input
                       })
    else:
        print('wrong ')
           
                   
def delete():
    delete_id = input('Delete:')
    for i in dict_list:
        if delete_id in i.values():
            dict_list.remove(i)

        
         

while True:
    print("""
          c -> create
          g -> get
          u -> update
          d -> delete
          e -> exit""")

    m = input('->')
   
    match m:
        case 'c':
            creat()
        case 'g':
            get_task()
        case 'u':
            update_id()
        case 'd':
            delete()
        case 'e':
            break
        case _:
            print('wrong input')
