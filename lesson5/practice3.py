def addtask():
    task ={
        "id" : input("id: "),
        "title" : input("title: "),
        "due_date" : input("due date: "),
         
    }
    tasks.append(task)
tasks=[]
addtask()
print(tasks)