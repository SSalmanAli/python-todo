<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 2.0.0
Modified principles:
- I. In-Memory Data Storage → I. Database Persistence with SQLModel and NeonDB
- II. Console-First Interface → II. REST API with FastAPI Framework
- IV. Clean Architecture & Separation of Concerns → IV. Clean Architecture with Service Layer
- V. Complete Feature Implementation → V. User-Scoped Task Operations
Added sections:
- VII. JWT-Based Authentication and Authorization
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->

# Python Todo Backend Service Constitution

## Core Principles

### I. Database Persistence with SQLModel and NeonDB
All tasks must be persisted in NeonDB (PostgreSQL) using SQLModel for ORM operations. The application must maintain data integrity, implement proper connection pooling, and follow ACID transaction principles. This ensures reliable data persistence, scalability, and enables proper user data isolation while maintaining consistent access to todo items.

### II. REST API with FastAPI Framework
All user interactions must occur through well-defined REST API endpoints following RESTful conventions. The API must provide six core endpoints: GET /tasks (list tasks), POST /tasks (create task), GET /tasks/{id} (retrieve task details), PUT /tasks/{id} (update task), DELETE /tasks/{id} (delete task), and PATCH /tasks/{id}/toggle (toggle completion status). API responses must be JSON-only with proper HTTP status codes.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced. All functionality must be covered by unit tests, integration tests, and API endpoint tests to ensure reliability and maintainability of the core todo operations and authentication mechanisms.

### IV. Clean Architecture with Service Layer
The codebase must follow clean code principles with clear separation between models (SQLModel data models), schemas (Pydantic request/response models), services (business logic layer extracted from original CLI app), database session management, configuration/security modules, and API route handlers. Each component should have a single responsibility and be independently testable with meaningful naming and small functions.

### V. User-Scoped Task Operations
All task operations must be scoped by user_id to ensure data isolation. The application must fully support all six required API endpoints: listing tasks (filtered by user_id), creating tasks (assigned to user_id), retrieving task details (with user_id validation), updating tasks (with user_id validation), deleting tasks (with user_id validation), and toggling task completion status (with user_id validation). Each task must have a unique ID and belong to a specific user.

### VI. Production-Quality Code Standards
All code must follow Python best practices, including proper type hints, comprehensive docstrings, error handling, and adherence to PEP 8 style guidelines. The implementation should be maintainable, readable, and demonstrate professional software engineering practices. Code must include proper logging, monitoring hooks, and follow security best practices.

### VII. JWT-Based Authentication and Authorization
Authentication must be enforced using JWT tokens provided by the frontend. The backend must validate JWT tokens and extract user identity for authorization purposes. The service must ensure that authenticated users can only access their own tasks by verifying user_id matches during all operations. Token validation must include signature verification, expiration checking, and proper error handling for invalid tokens.

## Data Model Requirements
Each task must contain: a unique ID (auto-generated), user_id (to scope tasks to specific users), title (required), description (optional), and completion status (boolean). The application must validate task data integrity, enforce foreign key relationships, and provide proper error messages for invalid inputs. All operations must maintain data consistency, prevent unauthorized access across user boundaries, and ensure proper indexing for performance.

## Development Workflow
The development flow follows spec-first approach: define behavior in specification, generate or refine implementation from the spec, and ensure the final running application demonstrably satisfies every defined behavior through API interactions. All changes must be small, testable, follow REST conventions, implement proper error handling, and reference code precisely. Development must include database migration strategies and API versioning considerations.

## Governance

This constitution defines the mandatory practices for the Python Todo Backend Service. All code changes must comply with these principles. Code reviews must verify adherence to clean architecture, proper testing, database schema changes, API endpoint design, and authentication/authorization requirements. Any deviation from these principles must be documented and approved.

**Version**: 2.0.0 | **Ratified**: 2026-01-06 | **Last Amended**: 2026-01-09
