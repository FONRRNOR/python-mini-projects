import os

FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                title, status = line.strip().split("|")
                tasks.append({"title": title, "done": status == "1"})
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            status = "1" if task["done"] else "0"
            f.write(f"{task['title']}|{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter new task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n==== TO-DO LIST MENU ====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()