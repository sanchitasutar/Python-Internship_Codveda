import json
file_name="todo_list.json"

def save_tasks(tasks) :
    try:
        with open (file_name,"w") as f:
            json.dump(tasks,f)      
    except:
        print("failed to saves")
        
def create_task(tasks):
    des=(input("enter task description :  ")) 
    print()
    if des:
        tasks["tasks"].append({"description":des,"complete":False})
        save_tasks(tasks) 
        print("tasks added")
    else :
        print("description cannot empty")  

 

def load_tasks():
    try:
        with open (file_name,"r") as f:
            return json.load(f)    
    except:
        return{"tasks":[]}   
def view(tasks) :
    print()
    task_list=tasks["tasks"]
    if len(task_list) ==0:
        print("no tasks")   
    else:
        print("To do list :")  
        for idx,task in enumerate(task_list):   #both idx nd value access kart: enumerate function
            status="[complete]" if task["complete"] else"[pending]"
            print(f"{idx+1}.{task['description']}|{status}") #idx+1 kely karn 1 pasun cnt chalu karaych like 1.task1..2.t2  
def mark_complete(tasks):
    view(tasks)
    try:
        task_no=int(input("enter task no = "))
        if 1<=task_no<=len(tasks):
            tasks["tasks"][task_no-1]["complete"]=True  # task-1 kelay karan index 0 pasun start hote ani apla task no 1 asto
            save_tasks(tasks) 
            print("Marked as complete")    
        else:
            print("invalid number")        
    except:
        ("invalid number") 

def main():
    tasks=load_tasks()
    while True:
        print("\n1.view\n2.Add\n3.complete\n4.Exit")
        ch=(input("enter ur choice="))
        if ch=="1":
            view(tasks)
        elif ch=="2":
            create_task(tasks)    
        elif ch=="3":
            mark_complete(tasks)
        elif ch=="4":
            print("goodby")
            break
main()              
