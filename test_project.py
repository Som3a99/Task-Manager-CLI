from project import add_task, complete_task, delete_task, tasks

def setup_function():
    tasks.clear()

def test_add_task():
    task = add_task("Test task", 1)
    assert task['id'] == 1
    assert len(tasks) == 1
    assert tasks[0]['description'] == "Test task"
    assert tasks[0]['priority'] == 1
    assert not tasks[0]['completed']

def test_complete_task():
    add_task("Test task", 1)
    assert complete_task(1)
    assert tasks[0]['completed']
    assert not complete_task(2)  # Invalid ID

def test_delete_task():
    add_task("Task 1", 1)
    add_task("Task 2", 2)
    assert delete_task(1)
    assert len(tasks) == 1
    assert not delete_task(999)  # Invalid ID
