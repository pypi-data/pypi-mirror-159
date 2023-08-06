# importing modules
import typer
from rich import print
from rich.table import Table
from tinydb import TinyDB, Query

app = typer.Typer() # app instance
db = TinyDB('coffee.db.json') # connecting with database

# commands

"""
Add command adds an task item into database
"""
"""
It takes only task as a parameter
"""
@app.command(name="add", short_help="Adds an item to you list")
def add(task: str):
    try:
        db.insert({'task': task})
        print(f":hot_beverage: [bold green]Added Task -[/bold green] {task}")
    except Exception as e:
        print(f":hot_beverage: [bold red]{e}[/bold red]")

"""
Update command updates an task item from database
"""
"""
It takes task id and new task as a parameter
"""
@app.command(name="update", short_help="Update an item")
def update(id: int, task: str = typer.Option(..., "--task")):
    try:
        _task = db.get(doc_id=id)
        db.update({'task': task}, doc_ids=[id] )
        print(f":hot_beverage: [bold green]Task Updated[/bold green] {_task['task']} to {task}")
    except Exception as e:
        print(f":hor_beverage: [bold red]{e}[/bold red]")

"""
Drop command deletes an task item from database
"""
"""
It takes task-id as a parameter
"""
@app.command(name="drop", short_help="Deletes an item")
def drop(id: int):
    try:
        task = db.get(doc_id=id)
        db.remove(doc_ids=[id])
        print(f":hot_beverage: [bold green]Task Removed -[/bold green] {task['task']}")
    except Exception as e:
        print(f":hot_beverage: [bold red]{e}[/bold red]")

"""
Tasks command let you see all your tasks.
It gets data from database and display in the form of table.
"""
"""
It does not take any parameter
"""
@app.command(name="tasks", short_help="Let you see your tasks")
def tasks():
    try:
        tasks = db.all()
        if (len(tasks) == 0):
            print(f":hot_beverage: [bold cyan]No Tasks! Add One[/bold cyan]")
        else:
            table = Table(title="Todo List", header_style="bold cyan")
            table.add_column("#", justify="left", style="cyan", no_wrap=True)
            table.add_column("Task", min_width=30)
            
            for index, task in enumerate(tasks):
                table.add_row(str(task.doc_id), task['task'])
            print(table)
    except Exception as e:
        print(f":hot_beverage: [bold red]{e}[/bold red]")

"""
Erase command removes all records from database
"""
"""
It does not take any parameter
"""
@app.command(name="erase", short_help="Removes all you task items")
def erase():
    try:
        db.truncate()
        print(":hot_beverage: [bold green]All Items Removed[/bold green]")
    except Exception as e:
        print(f":hot_beverage: [bold red]{e}[/bold red]")

if __name__ == "__main__":
    app() # calling app
