# Research: Python In-Memory Console Todo App

## Decision: Task Data Model
**Rationale**: Using a dataclass for the Task model provides clean, readable code with automatic generation of special methods like `__init__`, `__repr__`, and `__eq__`. This follows Python best practices and aligns with the clean code principles from the constitution.

**Alternatives considered**:
- Regular class with manual `__init__` method
- Named tuple (less flexible for updates)
- Dictionary (no type safety)

## Decision: CLI Framework
**Rationale**: Using Python's built-in `argparse` module for command-line parsing ensures we only use standard library components as required by the constitution. It's well-documented and provides all necessary functionality for a simple console application.

**Alternatives considered**:
- Click library (would require external dependency)
- Docopt (would require external dependency)
- Manual argument parsing (more error-prone)

## Decision: In-Memory Storage
**Rationale**: Using a simple list or dictionary for in-memory storage provides O(1) or O(n) operations as needed, with no external dependencies. A dictionary with task IDs as keys provides efficient lookup by ID for operations like update, delete, and mark.

**Alternatives considered**:
- External database (violates in-memory requirement)
- File storage (violates in-memory requirement)
- More complex data structures (unnecessary complexity)

## Decision: Task ID Generation
**Rationale**: Using a simple counter that increments for each new task ensures unique IDs with minimal complexity. The counter can be maintained as part of the TodoService state.

**Alternatives considered**:
- UUID (unnecessarily complex for this use case)
- Random number generation (potential for collisions)
- Timestamp-based IDs (potential for collisions in rapid operations)