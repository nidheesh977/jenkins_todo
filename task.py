tasks = []

def print_tasks(tasks):
    for task in tasks:
        print(task)

def create_task():
    global tasks
    tasks.append(input("Enter new task"))
    print_tasks(tasks)

def delete_task(index):
    global tasks
    tasks.pop(index)
    print_tasks(tasks)

def delete_all():
    global tasks
    tasks = []


create_task()