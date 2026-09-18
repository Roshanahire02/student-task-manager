FILE_NAME = "data/tasks.txt"


def add_task(task):
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")


def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks available. Add your first task!")
            return

        print("\nYour Tasks:")

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task.strip()}")

    except FileNotFoundError:
        print("No tasks available. Add your first task!")