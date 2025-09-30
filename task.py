tasks = []

def print_tasks(tasks):
    for task in tasks:
        print(task)

def create_task():
    tasks.append(input("Enter new task"))
    print_tasks(tasks)

create_task()