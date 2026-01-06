# Python Todo Console Application Constitution

## Core Principles

### I. In-Memory Data Storage
All tasks must be stored strictly in memory with no persistence to disk. The application must maintain data integrity during runtime and follow proper memory management practices. This ensures simplicity and avoids the complexity of database interactions while maintaining fast access to todo items.

### II. Console-First Interface
All user interactions must occur through a text-based console interface with clear prompts and readable output. The CLI must provide intuitive commands for all five required features: add, list, update, delete, and mark tasks. User experience should be clean and straightforward with proper error handling and helpful messages.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced. All functionality must be covered by unit tests to ensure reliability and maintainability of the core todo operations.

### IV. Clean Architecture & Separation of Concerns
The codebase must follow clean code principles with clear separation between models (task data structures), services (business logic), and CLI/entry point (user interface). Each component should have a single responsibility and be independently testable with meaningful naming and small functions.

### V. Complete Feature Implementation
The application must fully support all five basic features: adding tasks (with title and description), listing/viewing all tasks with clear status indicators (complete/incomplete), updating task details by ID, deleting tasks by ID, and marking tasks as complete or incomplete. Each task must have a unique ID for proper identification.

### VI. Production-Quality Code Standards
All code must follow Python best practices, including proper type hints, comprehensive docstrings, error handling, and adherence to PEP 8 style guidelines. The implementation should be maintainable, readable, and demonstrate professional software engineering practices.

## Data Model Requirements
Each task must contain: a unique ID (auto-generated), title (required), description (optional), and completion status (boolean). The application must validate task data integrity and provide proper error messages for invalid inputs. All operations must maintain data consistency and prevent duplicate IDs.

## Development Workflow
The development flow follows spec-first approach: define behavior in specification, generate or refine implementation from the spec, and ensure the final running application demonstrably satisfies every defined behavior through direct console interaction. All changes must be small, testable, and reference code precisely.

## Governance

This constitution defines the mandatory practices for the Python Todo Console Application. All code changes must comply with these principles. Code reviews must verify adherence to clean architecture, proper testing, and console interface requirements. Any deviation from these principles must be documented and approved.

**Version**: 1.0.0 | **Ratified**: 2026-01-06 | **Last Amended**: 2026-01-06
