# Task Manager CLI

[![Demo Video](https://img.shields.io/badge/View-Demo_Video-blue)](https://youtu.be/BOtKb6gUl-s)


A command-line task manager with persistent storage, built in Python.

## Features

- **Add Tasks**: Specify descriptions and priorities.
- **List Tasks**: View all tasks with IDs, priorities, and completion status.
- **Complete/Delete Tasks**: Mark tasks as completed or remove them entirely.
- **Data Persistence**: Tasks are saved to a JSON file and retained between sessions.
- **Testing**: Includes pytest test suite for core functions.

## Usage

* Add a task with priority
```bash
python project.py add "Write project report" --priority 2
```
* List all tasks
```bash
python project.py list
```
* Mark task #1 as completed
```bash
python project.py complete 1
```
* Delete task #1
```bash
python project.py delete 1
```

## Testing
```bash
pytest test_project.py -v
```
