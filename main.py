todo_list=[]
def add_tesk(todo_list:list,task:str):
    todo_list.append(task)
    return todo_list

# adding_tasks=add_tesk(todo_list,tesk_input)


def showing_list(todo_list):
    index=0
    if len(todo_list) == 0:
        print("no items")
         
    for i in todo_list:
        index+=1
        print (str(index)+":",i)


def get_user_choice():
    flag=True
    user_choice = ""
    while flag:
        try:
            user_choice=int(input("""Hey what would you like to do? 
        1.Add task
        2.View list
        3.Exit
        :"""))
        except:
            print("wrong choice!")
        match user_choice:
            case 1: 
                add_tesk(todo_list,input("enter a tesk:"))
            case 2:
                showing_list(todo_list)
            case 3:
                flag=False
                print("bye bye")
                
            
        
        
get_user_choice()


