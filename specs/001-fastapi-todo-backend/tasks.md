# Tasks: FastAPI Todo Backend Service

## Feature Overview
Convert the existing Python CLI Todo application into a FastAPI-based RESTful service using SQLModel and NeonDB for persistent storage. The backend exposes JWT-protected endpoints scoped by user_id to create, list, retrieve, update, delete, and toggle completion of tasks, ensuring users can access only their own data.

## Implementation Strategy
- **MVP Scope**: Start with User Story 1 (Core task operations) to create a minimal viable product
- **Incremental Delivery**: Build foundational components first, then add user stories in priority order
- **Parallel Execution**: Identified tasks that can be worked on simultaneously (marked with [P])
- **Independent Testing**: Each user story is designed to be independently testable

---

## Phase 1: Setup

### Goal
Initialize project structure and install dependencies as specified in the implementation plan.

- [x] T001 Create backend/ directory structure with src/, tests/, requirements.txt, requirements-dev.txt
- [x] T002 Create requirements.txt with FastAPI, SQLModel, NeonDB (asyncpg), PyJWT, python-multipart
- [x] T003 Create requirements-dev.txt with pytest, httpx, pytest-asyncio for testing
- [x] T004 Create alembic directory structure with env.py, script.py.mako, README, alembic.ini, versions/
- [x] T005 Create directory structure inside backend/src/: main.py, config/, models/, schemas/, services/, api/, and subdirectories

## Phase 2: Foundational Components

### Goal
Establish foundational components that block all user stories: database connectivity, authentication, and application entry point.

- [x] T006 [P] Create backend/src/main.py with FastAPI app initialization and health check endpoint
- [x] T007 [P] Create backend/src/config/settings.py for environment configuration
- [x] T008 [P] Create backend/src/config/database.py with SQLModel engine and session management
- [x] T009 [P] Create backend/src/config/security.py with JWT token handling utilities
- [x] T010 [P] Create backend/tests/conftest.py with test fixtures for database and app testing
- [x] T011 [P] Create backend/tests/test_main.py with health check tests

## Phase 3: User Story 1 - Create and Manage Personal Tasks (Priority: P1)

### Goal
Enable authenticated users to create, view, update, delete, and toggle completion status of their personal tasks through REST API endpoints.

**Independent Test Criteria**: API can be fully tested by making authenticated requests to create, list, update, delete, and toggle task completion. Each operation validates that users can only access their own data and that all CRUD operations work correctly.

- [x] T012 [P] [US1] Create backend/src/models/task.py with SQLModel Task entity and database schema
- [x] T013 [P] [US1] Create backend/src/schemas/task.py with Pydantic schemas for task operations
- [x] T014 [P] [US1] Create backend/src/services/task_service.py with business logic extracted from CLI implementation
- [x] T015 [US1] Create backend/src/api/routes/tasks.py with basic task CRUD endpoints
- [x] T016 [US1] Implement GET /tasks endpoint to list user's tasks
- [x] T017 [US1] Implement POST /tasks endpoint to create new tasks
- [x] T018 [US1] Implement GET /tasks/{id} endpoint to retrieve specific task
- [x] T019 [US1] Implement PUT /tasks/{id} endpoint to update tasks
- [x] T020 [US1] Implement DELETE /tasks/{id} endpoint to delete tasks
- [x] T021 [US1] Implement PATCH /tasks/{id}/toggle endpoint to toggle completion status
- [x] T022 [P] [US1] Create backend/tests/test_task_models.py with model validation tests
- [x] T023 [P] [US1] Create backend/tests/test_task_schemas.py with schema validation tests
- [x] T024 [P] [US1] Create backend/tests/test_task_service.py with business logic tests
- [x] T025 [US1] Create backend/tests/test_task_routes.py with API endpoint tests for CRUD operations

## Phase 4: User Story 2 - Secure Data Access (Priority: P2)

### Goal
Implement JWT authentication and authorization mechanisms that ensure users can only access and modify their own tasks.

**Independent Test Criteria**: System can be tested by attempting to access other users' tasks with different JWT tokens, ensuring that unauthorized access is prevented and appropriate error responses are returned.

- [x] T026 [P] [US2] Enhance backend/src/config/security.py with JWT token validation middleware
- [x] T027 [US2] Add JWT authentication dependency to all task endpoints
- [x] T028 [US2] Implement user_id scoping validation in task service layer
- [x] T029 [US2] Add 401 Unauthorized responses for invalid/missing JWT tokens
- [x] T030 [US2] Add 403 Forbidden responses for unauthorized task access attempts
- [x] T031 [P] [US2] Create backend/tests/test_security.py with JWT authentication tests
- [x] T032 [US2] Add security tests for cross-user access prevention
- [x] T033 [US2] Create mock JWT tokens for testing different user contexts

## Phase 5: User Story 3 - Persistent Data Storage (Priority: P3)

### Goal
Ensure tasks are reliably stored in NeonDB using SQLModel and maintained persistently across server restarts.

**Independent Test Criteria**: System can be validated by creating tasks, restarting the service, and verifying that all data remains accessible and unchanged for authenticated users.

- [x] T034 [P] [US3] Implement database connection pooling in backend/src/config/database.py
- [x] T035 [US3] Add database initialization and migration support with Alembic
- [x] T036 [US3] Create database migration files for Task model
- [x] T037 [US3] Add transaction management and error handling to task service
- [x] T038 [US3] Implement proper database session management in API routes
- [x] T039 [P] [US3] Create backend/tests/test_database.py with database connectivity tests
- [x] T040 [US3] Add tests for data persistence across restarts
- [x] T041 [US3] Add database error handling and retry logic

## Phase 6: Polish & Cross-Cutting Concerns

### Goal
Address edge cases, error handling, and cross-cutting concerns to complete the implementation.

- [x] T042 [P] Add comprehensive error handling with proper HTTP status codes
- [x] T043 [P] Implement input validation and sanitization
- [x] T044 [P] Add logging and monitoring hooks throughout the application
- [x] T045 [P] Add rate limiting and request throttling
- [x] T046 [P] Create backend/tests/test_error_handling.py with error scenario tests
- [x] T047 [P] Add comprehensive documentation and API examples
- [x] T048 [P] Add environment-specific configuration for dev/staging/prod
- [x] T049 [P] Add performance monitoring and metrics collection
- [x] T050 [P] Final integration testing and end-to-end validation

---

## Dependencies

### User Story Completion Order
1. **User Story 1 (P1)**: Core functionality - Create and Manage Personal Tasks
2. **User Story 2 (P2)**: Security - Secure Data Access (depends on US1)
3. **User Story 3 (P3)**: Persistence - Persistent Data Storage (depends on US1)

### Critical Path Dependencies
- Foundational components (database, security, main app) must be completed before user stories
- User Story 1 must be completed before User Story 2 and 3 can be fully tested
- Database migration setup (T035-T036) must be done before production deployment

## Parallel Execution Opportunities

### Within User Story 1
- Models, schemas, and services can be developed in parallel ([P] tasks T012-T014)
- Individual endpoints can be developed incrementally (T015-T021)
- Unit tests can be written in parallel with implementation ([P] tasks T022-T024)

### Across User Stories
- Security enhancements (US2) can begin once core functionality (US1) models and services are established
- Database optimizations (US3) can run alongside security implementation
- Testing can be parallelized across all components

## Acceptance Criteria

### User Story 1 (P1) - Core Task Operations
- [ ] Users can create tasks via POST /tasks with proper JWT authentication
- [ ] Users can list their own tasks via GET /tasks
- [ ] Users can retrieve specific task details via GET /tasks/{id}
- [ ] Users can update tasks via PUT /tasks/{id}
- [ ] Users can delete tasks via DELETE /tasks/{id}
- [ ] Users can toggle task completion via PATCH /tasks/{id}/toggle

### User Story 2 (P2) - Security
- [ ] All endpoints require valid JWT tokens
- [ ] Users cannot access tasks belonging to other users
- [ ] Appropriate 401/403 responses are returned for unauthorized access
- [ ] JWT tokens are properly validated for signature and expiration

### User Story 3 (P3) - Persistence
- [ ] Tasks are stored permanently in NeonDB
- [ ] Data survives server restarts
- [ ] Database operations are efficient with proper indexing
- [ ] Transaction integrity is maintained for all operations