todo_list=[]
def add_tesk(todo_list:list,task:str):
    todo_list.append(task)
    return todo_list
tesk_input=input("enter a tesk:")
adding_tasks=add_tesk(todo_list,tesk_input)

