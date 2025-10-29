todo_list=[]
def adding_items(todo_list):
    user_item=input("please add a task:")
    
    todo_list.append(user_item)
    


def showing_list(todo_list):
    index=0
    if len(todo_list) == 0:
        print("no items")
         
    for i in todo_list:
        index+=1
        print (index,i)
    




