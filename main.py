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


def menu():
    flag=True
    while flag:
        user_choice=int(input("""Hey what would you like to do? 
        1.Add task
        2.View list
        3.Exit
        :"""))
        match user_choice:
            case 1: 
                adding_items(todo_list)
            case 2:
                showing_list(todo_list)
            case 3:
                flag=False
                print("bye bye")
                
            
        
        



