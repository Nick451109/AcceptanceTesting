from behave import given, when, then
from todo_list import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo = ToDoList()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.todo.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = [t['task'] for t in context.todo.list_tasks()]
    assert task in tasks, f"Expected task '{task}' not found in the to-do list."

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.tasks_output = context.todo.list_tasks()

@then('the output should contain')
def step_impl(context):
    expected_tasks = [row['Tasks'] for row in context.table]
    actual_tasks = [t['task'] for t in context.tasks_output]
    for task in expected_tasks:
        assert task in actual_tasks, f"Expected task '{task}' not found in the output."

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    # Find the task number by task name
    task_number = next((i + 1 for i, t in enumerate(context.todo.list_tasks()) if t['task'] == task), None)
    if task_number is not None:
        context.todo.mark_task_completed(task_number)
    else:
        raise AssertionError(f"Task '{task}' not found in the to-do list.")

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.todo.list_tasks():
        if t['task'] == task:
            assert t['status'] == "Completed", f"Expected task '{task}' to be completed."

@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert context.todo.list_tasks() == [], "Expected the to-do list to be empty."
