import json
from InquirerPy import inquirer
import sys
print("===todo-cli===")
choice = inquirer.select(
    message="Select an option",
    choices=["Add","Remove","Exit"],
    pointer=">",
).execute()

def a():
    Group = ""
    Task = ""
    while Group == "" or Task == "":
        Group = input("Group: ")
        if Group == "":
            print("Input a group name")
            continue
        Task = input("Task: ")
        if Task == "":
            print("Input a task name")
            continue
    with open("todo.json", "r") as file:
        jsontext = file.read()
        data = json.loads(jsontext)
        if Group in data:
            data[Group].append(Task)
        else:
            data[Group] = [Task]
    with open("todo.json", "w") as file:
        update_json = json.dump(data, file, indent=4)
        print(data)

def r():
    Group = ""
    Task = ""
    with open("todo.json", "r") as file:
        jsontext = file.read()
        data = json.loads(jsontext)
        print(data)
        while Group == "" or Task == "":
            Group = input("Group: ")
            if Group == "":
                print("Input a group name")
                continue
            Task = input("Task: ")
            if Task == "":
                print("Input a task name")
                continue
        if Group in data:
            data[Group].remove(Task)
        else:
            print(f"{Group} doesnt exsist")
    with open("todo.json", "w") as file:
        update_json = json.dump(data, file, indent=4)
        print(data)
        

def e():
    sys.exit()

actions = {
    "Add": a,
    "Remove": r,
    "Exit": e,
}
actions[choice]()
