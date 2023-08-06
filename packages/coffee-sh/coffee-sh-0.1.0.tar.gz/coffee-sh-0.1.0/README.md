# Coffee.sh

Coffee is a command-line utility for developers who want their task list at terminal

## Installation

```bash
pip install coffee-sh
```

## Usage

To add a new task

```bash
coffee add "Drink Water"
```

To Update task

```bash
coffee update 1 --task "Drink More Water"
```

> Here 1 is task ID which is unique

To Delete task

```bash
coffee drop 1
```

> Here 1 is task ID which is unique

To show all tasks

```
coffee tasks
```

To remove all tasks
```bash
coffee erase
```
