---
description: "Task list for Python In-Memory Console Todo App implementation"
---

# Tasks: Python In-Memory Console Todo App

**Input**: Design documents from `/specs/1-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan in src/, tests/
- [x] T002 Initialize Python project with proper directory structure
- [x] T003 [P] Configure linting and formatting tools (flake8, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task data model in src/models/task.py
- [x] T005 Create TodoService class in src/services/todo_service.py
- [x] T006 Create CLI argument parser in src/cli/todo_cli.py
- [x] T007 Setup main entry point in src/__main__.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to create new tasks with title and optional description

**Independent Test**: User can run the add command with a title and description, and the task appears in the list with a unique ID and incomplete status

### Implementation for User Story 1

- [x] T008 [P] [US1] Implement Task data model with ID, title, description, completed fields in src/models/task.py
- [x] T009 [P] [US1] Implement add_task method in TodoService in src/services/todo_service.py
- [x] T010 [US1] Add 'add' command to CLI parser in src/cli/todo_cli.py
- [x] T011 [US1] Implement add command handler in src/cli/todo_cli.py
- [x] T012 [US1] Connect add command to service in src/__main__.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to see all their tasks with clear status indicators

**Independent Test**: User can run the list command and see all tasks with unique IDs, titles, descriptions, and clear complete/incomplete indicators

### Implementation for User Story 2

- [x] T013 [P] [US2] Implement get_all_tasks method in TodoService in src/services/todo_service.py
- [x] T014 [US2] Add 'list' command to CLI parser in src/cli/todo_cli.py
- [x] T015 [US2] Implement list command handler in src/cli/todo_cli.py
- [x] T016 [US2] Connect list command to service in src/__main__.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Enable users to modify an existing task's title or description

**Independent Test**: User can run the update command with a specific task ID to change the task's information and verify changes are reflected

### Implementation for User Story 3

- [x] T017 [P] [US3] Implement update_task method in TodoService in src/services/todo_service.py
- [x] T018 [US3] Add 'update' command to CLI parser in src/cli/todo_cli.py
- [x] T019 [US3] Implement update command handler in src/cli/todo_cli.py
- [x] T020 [US3] Connect update command to service in src/__main__.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Mark Tasks Complete/Incomplete (Priority: P2)

**Goal**: Enable users to mark a task as complete when finished, or mark it as incomplete if they need to work on it again

**Independent Test**: User can run the mark command with a specific task ID and completion status and verify the status change

### Implementation for User Story 4

- [x] T021 [P] [US4] Implement mark_task method in TodoService in src/services/todo_service.py
- [x] T022 [US4] Add 'mark' command to CLI parser in src/cli/todo_cli.py
- [x] T023 [US4] Implement mark command handler in src/cli/todo_cli.py
- [x] T024 [US4] Connect mark command to service in src/__main__.py

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Enable users to remove a task from their list when it's no longer needed

**Independent Test**: User can run the delete command with a specific task ID to remove the task and verify it no longer appears in the list

### Implementation for User Story 5

- [x] T025 [P] [US5] Implement delete_task method in TodoService in src/services/todo_service.py
- [x] T026 [US5] Add 'delete' command to CLI parser in src/cli/todo_cli.py
- [x] T027 [US5] Implement delete command handler in src/cli/todo_cli.py
- [x] T028 [US5] Connect delete command to service in src/__main__.py

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T029 [P] Add comprehensive error handling across all operations
- [x] T030 [P] Add input validation for all commands
- [x] T031 [P] Add docstrings and type hints to all functions
- [x] T032 Add help text and usage examples to CLI
- [x] T033 Run quickstart.md validation
- [x] T034 Create README.md with usage instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement Task data model with ID, title, description, completed fields in src/models/task.py"
Task: "Implement add_task method in TodoService in src/services/todo_service.py"
Task: "Add 'add' command to CLI parser in src/cli/todo_cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence