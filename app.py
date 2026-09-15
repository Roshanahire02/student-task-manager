from tasks import add_task, view_tasks


def main():
    while True:
        print("\n===== STUDENT TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()