# Python In-Memory Console Todo App

A simple, in-memory console-based todo application built with Python. This application allows you to manage your tasks directly from the command line without any persistence beyond runtime memory.

## Features

- **Interactive Console Mode**: Easy-to-use menu-driven interface
- Add new tasks with titles and optional descriptions
- List all tasks with clear status indicators
- Update existing task details
- Mark tasks as complete or incomplete
- Delete tasks
- All data stored in memory only (no persistence beyond runtime)

## Requirements

- Python 3.8 or higher
- Node.js & npm (optional, for convenience scripts)

## Quick Start

Run the interactive application:

```bash
npm run dev
```

Or using Python directly:

```bash
python -m src
```

## Usage

### Interactive Mode
Simply run `npm run dev` to enter the interactive menu:
1. Navigate options using the number keys.
2. Follow the on-screen prompts to manage tasks.
3. Select 'Exit' to close the application.

### Command Line Mode
You can still use individual commands by passing arguments.

**Add a new task:**
```bash
npm run dev -- add --title "Task Title" --description "Task Description"
```

**List all tasks:**
```bash
npm run dev -- list
```

**Update a task:**
```bash
npm run dev -- update --id 1 --title "New Title" --description "New Description"
```

**Mark a task as complete:**
```bash
npm run dev -- mark --id 1 --status complete
```

**Delete a task:**
```bash
npm run dev -- delete --id 1
```

## Architecture

The application follows clean architecture principles:

- **Models** (`src/models/`): Data structures (Task model)
- **Services** (`src/services/`): Business logic (TodoService)
- **CLI** (`src/cli/`): Command-line interface
- **Entry Point** (`src/__main__.py`): Application entry point

## Design Principles

- In-memory storage only (no persistence beyond runtime)
- Console-first interface with clear prompts
- Clean separation of concerns
- Production-quality code standards
- Follows Python best practices (PEP 8, type hints, etc.)