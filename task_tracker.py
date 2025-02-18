# %%
#I am going to use python to create a CLI app to track my tasks. 
import argparse
import json
import os
import time

# %%

timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#step 1, check if there is a json file, if not create one

if os.path.exists("tasks.json") == False:
    print("JSON file doesn't exist, creating one now")
    with open("tasks.json", "w",encoding="utf-8") as file:
        file.write("{}")
else:
    print("JSON exists")


# %%


def add(description: str, status: str):
    '''this function will add a task to the json file'''
    task = {
    "description": description,
    "status": status,
    "created_at": timestamp,
    "updated_at": timestamp
    }
    
    with open("tasks.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)
        
    id = len(tasks) + 1
    if str(id) in tasks:
        id += int(max(tasks.keys()))+1
    tasks[id] = task
    
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
        
    print("Task added successfully")


# %%
def update(id: int, description: str | None = None, status: str | None = None):
    '''this function will update a task in the json file'''
    with open("tasks.json", "r") as file:
        tasks = json.load(file)  
    if str(id) not in tasks:
        print("Task not found")
    else:
        tasks[str(id)]["description"] = description
        tasks[str(id)]["status"] = status
        tasks[str(id)]["updated_at"] = timestamp
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        print("Task updated successfully")

update(2, "task1", "done")


# %%
def delete(id: int):
    '''this function will delete a task in the json file'''
    with open("tasks.json", "r") as file:
        tasks = json.load(file)  
    del tasks[str(id)]
    
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
        
    print("Task deleted successfully")

# %%
def list():
    '''this function will list all the tasks in the json file'''
    with open("tasks.json", "r") as file:
        tasks = json.load(file)  
    for i in tasks:
        print(f"id: {i}") 
        print(tasks[i])

# %%
def list_done():
    '''this function will list all the tasks with status donein the json file'''
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for i in tasks:
        if tasks[i]["status"] == "done":
            print(f"id: {i}") 
            print(tasks[i])


# %%
def list_todo():
    '''this function will list all the tasks with status donein the json file'''
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for i in tasks:
        if tasks[i]["status"] == "todo":
            print(f"id: {i}") 
            print(tasks[i])
            

# %%
def list_in_progress():
    '''this function will list all the tasks with status donein the json file'''
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    for i in tasks:
        if tasks[i]["status"] == "in_progress":
            print(f"id: {i}") 
            print(tasks[i])
            

# %%
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="一个简单的 CLI 示例")
    parser.add_argument("action", help="add, update, delete, list, list_done, list_todo, list_in_progress")
    
    parser.add_argument("--id", type=int, help="任务 ID")
    parser.add_argument("--description", help="任务描述")
    parser.add_argument("--status", help="任务状态")
    
    args = parser.parse_args()
    
    if args.action == "add":
        add(args.description, args.status)
    elif args.action == "update":
        update(args.id, args.description, args.status)
    elif args.action == "delete":
        delete(args.id)
    elif args.action == "list":
        list()
    elif args.action == "list_done":
        list_done()
    elif args.action == "list_todo":
        list_todo()
    elif args.action == "list_in_progress":
        list_in_progress()
    else:
        print("Invalid action")
        
        



# %%
