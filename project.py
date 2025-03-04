import argparse
import json

tasks = []


def main():
    load_tasks()
    parser = argparse.ArgumentParser(
        prog='Task Management CLI',
        description='Task Manager using CLI command line interface'
    )
    subparsers = parser.add_subparsers(dest='command', help='Avaliable commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument("description", type=str, help='Task description')
    add_parser.add_argument("--priority", type=int, default=1, help='Task priority by default: 1')

    # List command
    subparsers.add_parser('list', help='List all tasks')

    # complete command
    parser_complete = subparsers.add_parser('complete', help='Mark a task as complete')
    parser_complete.add_argument('task_id', type=int, help='ID of the task to complete')

    # Delete command
    parser_Delete = subparsers.add_parser('delete', help='Delete a task')
    parser_Delete.add_argument('task_id', type=int, help='ID of the task to delete')

    args = parser.parse_args()
    modified = False

    if args.command == 'add':
        add_task(args.description, args.priority)
        print(f"Task added with ID {tasks[-1]['id']}")
        modified = True
    elif args.command == 'list':
        if not tasks:
            print("No tasks found")
        else:
            for task in tasks:
                status = 'completed' if task['completed'] else 'pending'
                print(f"ID: {task['id']}, Description: {task['description']}, Priority: {task['priority']}, Status: {status}.")
    elif args.command == 'complete':
        success = complete_task(args.task_id)
        if success:
            print(f"Task {args.task_id} marked as completed")
            modified = True
        else:
            print(f"Task {args.task_id} not found")
    elif args.command == 'delete':
        success = delete_task(args.task_id)
        if success:
            print(f"Task {args.task_id} deleted")
            modified = True
        else:
            print(f"Task {args.task_id} not found")
    else:
        parser.print_help()

    if modified:
        save_tasks()


def add_task(description, priority):
    if not tasks:
        new_id = 1
    else:
        new_id = max(task['id'] for task in tasks) + 1
    task = {
        'id': new_id,
        'description': description,
        'priority': priority,
        'completed': False,
    }
    tasks.append(task)
    return task


def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            if not task['completed']:
                task['completed'] = True
                return True
            return False
        return False


def delete_task(task_id):
    before = len(tasks)
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    return len(tasks) < before


def save_tasks():
    with open("tasks.json", 'w') as f:
        json.dump(tasks, f)


def load_tasks():
    global tasks
    try:
        with open("tasks.json", 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

if __name__=="__main__":
    main()
