# Quickstart: Python In-Memory Console Todo App

## Getting Started

1. **Run the application**:
   ```bash
   python -m src
   ```

2. **Available Commands**:
   - `add --title "Task Title" [--description "Task Description"]` - Add a new task
   - `list` - View all tasks with status indicators
   - `update --id ID [--title "New Title"] [--description "New Description"]` - Update a task
   - `delete --id ID` - Delete a task
   - `mark --id ID --status [complete|incomplete]` - Mark task as complete/incomplete
   - `help` - Show available commands

## Example Usage

### Add a new task:
```bash
python -m src add --title "Buy groceries" --description "Milk, bread, eggs"
```

### List all tasks:
```bash
python -m src list
```

### Update a task:
```bash
python -m src update --id 1 --title "Buy groceries and cook dinner"
```

### Mark a task as complete:
```bash
python -m src mark --id 1 --status complete
```

### Delete a task:
```bash
python -m src delete --id 1
```

## Project Structure

```
src/
├── models/
│   └── task.py          # Task data model
├── services/
│   └── todo_service.py  # Business logic
├── cli/
│   └── todo_cli.py      # Command-line interface
└── __main__.py          # Entry point
```