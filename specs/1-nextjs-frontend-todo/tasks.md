---
description: "Task list for Next.js frontend Todo application implementation"
---

# Tasks: Next.js Frontend Todo Application

**Input**: Design documents from `/specs/1-nextjs-frontend-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `frontend/src/`, `frontend/public/`
- Paths shown below based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create Next.js project structure with TypeScript and App Router
- [ ] T002 [P] Configure package.json with Next.js, React, Tailwind CSS dependencies
- [ ] T003 [P] Set up TypeScript configuration (tsconfig.json)
- [ ] T004 [P] Configure Tailwind CSS and global styles (globals.css)
- [ ] T005 Create environment variable configuration (.env.example)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 [P] Install and configure BetterAuth for authentication
- [ ] T007 [P] Create centralized API client with JWT token attachment in frontend/src/lib/api/client.ts
- [ ] T008 [P] Create authentication context/provider in frontend/src/providers/AuthProvider.tsx
- [ ] T009 [P] Create custom authentication hook in frontend/src/hooks/useAuth.ts
- [ ] T010 [P] Define TypeScript types for Task and UserSession in frontend/src/lib/types/
- [ ] T011 Create route protection middleware for authenticated routes
- [ ] T012 Set up base layout structure in frontend/src/app/layout.tsx

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Authenticate and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable authenticated users to log in and view their list of tasks retrieved from the backend

**Independent Test**: User can log in with valid credentials and see their list of tasks from the backend

### Implementation for User Story 1

- [ ] T013 [P] Create login page component in frontend/src/app/(auth)/login/page.tsx
- [ ] T014 [P] Create authentication UI components in frontend/src/components/auth/
- [ ] T015 Create dashboard layout for authenticated users in frontend/src/app/dashboard/layout.tsx
- [ ] T016 [P] Create TaskList component to display tasks in frontend/src/components/tasks/TaskList.tsx
- [ ] T017 [P] Create TaskCard component to display individual tasks in frontend/src/components/tasks/TaskCard.tsx
- [ ] T018 Create tasks API functions in frontend/src/lib/api/tasks.ts
- [ ] T019 Implement task fetching logic in frontend/src/app/dashboard/page.tsx
- [ ] T020 Add loading and error state handling to task list view
- [ ] T021 Wire authentication flow to BetterAuth and store JWT token
- [ ] T022 Implement route protection to redirect unauthenticated users to login

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Create New Tasks (Priority: P2)

**Goal**: Allow authenticated users to create new tasks with title and description that persist in the backend

**Independent Test**: User can create a new task and verify it appears in the task list and persists in the backend

### Implementation for User Story 2

- [ ] T023 [P] Create TaskForm component in frontend/src/components/tasks/TaskForm.tsx
- [ ] T024 Implement task creation API call in frontend/src/lib/api/tasks.ts
- [ ] T025 Add task creation form to dashboard page in frontend/src/app/dashboard/page.tsx
- [ ] T026 Add client-side validation to task form
- [ ] T027 Update task list UI to reflect newly created tasks without refresh
- [ ] T028 Handle error states during task creation

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Manage Existing Tasks (Priority: P3)

**Goal**: Enable authenticated users to update, delete, and toggle completion status of existing tasks

**Independent Test**: User can perform update, delete, and toggle operations on existing tasks

### Implementation for User Story 3

- [ ] T029 [P] Enhance TaskCard component with edit/delete/toggle controls in frontend/src/components/tasks/TaskCard.tsx
- [ ] T030 [P] Add task update API function in frontend/src/lib/api/tasks.ts
- [ ] T031 [P] Add task delete API function in frontend/src/lib/api/tasks.ts
- [ ] T032 [P] Add task toggle completion API function in frontend/src/lib/api/tasks.ts
- [ ] T033 Implement inline editing functionality for tasks
- [ ] T034 Add confirmation dialog for task deletion
- [ ] T035 Update UI state immediately on successful operations without refresh
- [ ] T036 Handle success/error feedback for all task management operations

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T037 [P] Add empty state handling to task list
- [ ] T038 [P] Implement consistent loading states across all views
- [ ] T039 Add error boundary components for robust error handling
- [ ] T040 Add responsive design enhancements for mobile devices
- [ ] T041 [P] Add accessibility attributes to all UI components
- [ ] T042 Add proper meta tags and SEO considerations
- [ ] T043 [P] Add unit tests for API client and utility functions
- [ ] T044 Run quickstart validation and fix any issues

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
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Builds on US1 authentication and task list
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Builds on US1 authentication and task list

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members

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
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence