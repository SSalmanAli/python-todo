# Data Model: Python In-Memory Console Todo App

## Task Entity

### Fields
- **id**: `int` - Unique identifier automatically assigned when task is created
- **title**: `str` - Required task title (cannot be empty)
- **description**: `str` - Optional task description (can be empty or None)
- **completed**: `bool` - Task completion status (default: False)

### Validation Rules
- **id**: Must be unique within the task collection, auto-generated
- **title**: Must not be None or empty string after stripping whitespace
- **description**: Optional, can be None or any string value
- **completed**: Must be boolean value (True or False)

### State Transitions
- **Creation**: New task created with `completed = False` by default
- **Update**: Title and description can be modified by user
- **Mark Complete**: `completed` transitions from `False` to `True`
- **Mark Incomplete**: `completed` transitions from `True` to `False`

## TaskList Collection

### Structure
- **tasks**: `dict[int, Task]` - Dictionary mapping task IDs to Task objects
- **next_id**: `int` - Counter for generating unique IDs (starts at 1, increments)

### Operations
- **Add Task**: Insert new Task with unique ID
- **Get Task**: Retrieve Task by ID
- **Update Task**: Modify existing Task by ID
- **Delete Task**: Remove Task by ID
- **List Tasks**: Return all Tasks
- **Mark Task**: Update completion status by ID