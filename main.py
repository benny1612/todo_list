todo_list=[]
def adding_items(todo_list):
    user_item=input("please add a task:")
    todo_list.append(user_item)
    return todo_list
adding_tasks=adding_items(todo_list)