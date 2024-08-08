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
    assert task in tasks

@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row['Task'])

@then('the output should contain:')
def step_impl(context):
    tasks = [t['task'] for t in context.todo.list_tasks()]
    for row in context.table:
        assert row['Tasks'] in tasks

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.todo.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for t in context.todo.list_tasks():
        if t['task'] == task:
            assert t['status'] == "Completed"

@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert context.todo.list_tasks() == []
