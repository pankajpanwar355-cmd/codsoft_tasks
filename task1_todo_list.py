import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        try:
            return json.loads(DATA_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("Saved task data could not be read. Starting with an empty list.")
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=4), encoding="utf-8")


def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n------ YOUR TO-DO LIST ------")
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f'{number}. {task["title"]} [{status}]')
    print("-----------------------------")


def get_task_number(tasks):
    try:
        number = int(input("Enter task number: "))
        if 1 <= number <= len(tasks):
            return number - 1
        print("That task number does not exist.")
    except ValueError:
        print("Please enter a valid number.")
    return None


def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Mark task as complete / pending")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            title = input("Enter the new task: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                save_tasks(tasks)
                print("Task added successfully.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                index = get_task_number(tasks)
                if index is not None:
                    new_title = input("Enter the updated task: ").strip()
                    if new_title:
                        tasks[index]["title"] = new_title
                        save_tasks(tasks)
                        print("Task updated successfully.")
                    else:
                        print("Task cannot be empty.")

        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                index = get_task_number(tasks)
                if index is not None:
                    tasks[index]["completed"] = not tasks[index]["completed"]
                    save_tasks(tasks)
                    print("Task status changed.")

        elif choice == "5":
            show_tasks(tasks)
            if tasks:
                index = get_task_number(tasks)
                if index is not None:
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f'Task "{removed["title"]}" deleted.')

        elif choice == "6":
            print("Thank you for using the To-Do List.")
            break

        else:
            print("Invalid choice. Please choose from 1 to 6.")


if __name__ == "__main__":
    main()
