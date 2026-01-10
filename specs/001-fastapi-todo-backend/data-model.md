# Data Model: FastAPI Todo Backend Service

## Task Entity

### Fields
- **id** (Integer, Primary Key, Auto-generated)
  - Unique identifier for each task
  - Auto-incremented integer value
  - Required field

- **user_id** (String/UUID, Indexed)
  - Foreign key linking task to user
  - Used for enforcing user scoping
  - Required field for data isolation

- **title** (String, Max 255 characters)
  - Brief description of the task
  - Required field
  - Must not be empty

- **description** (String, Optional, Max 1000 characters)
  - Detailed information about the task
  - Optional field
  - Can be null/empty

- **completed** (Boolean)
  - Status indicator for task completion
  - Default: False
  - Required field

- **created_at** (DateTime, Indexed)
  - Timestamp when task was created
  - Auto-populated on creation
  - Required field

- **updated_at** (DateTime)
  - Timestamp when task was last modified
  - Auto-updated on changes
  - Required field

### Relationships
- **User** (Many-to-One)
  - Each task belongs to one user
  - User can have many tasks
  - Enforced through user_id foreign key

### Validation Rules
- Title must be 1-255 characters
- Description, if provided, must be ≤ 1000 characters
- user_id must exist in users table (foreign key constraint)
- All tasks must have a valid user_id
- completed field must be boolean (true/false)

### State Transitions
- **New Task**: created with completed=False
- **Completed**: transition from completed=False to completed=True
- **Reopened**: transition from completed=True to completed=False
- **Deleted**: soft delete with deleted_at timestamp (optional future enhancement)

## Indexes
- **idx_user_id**: Index on user_id for efficient user-scoped queries
- **idx_created_at**: Index on created_at for chronological sorting
- **idx_user_completed**: Composite index on (user_id, completed) for filtered queries

## Constraints
- **PK**: PRIMARY KEY (id)
- **FK**: FOREIGN KEY (user_id) REFERENCES users(id)
- **NN**: NOT NULL constraints on id, user_id, title, completed, created_at
- **CHK**: CHECK (LENGTH(title) > 0) for non-empty titles

## Sample Data Structure
```json
{
  "id": 123,
  "user_id": "user-uuid-string",
  "title": "Complete project proposal",
  "description": "Finish the technical specifications document",
  "completed": false,
  "created_at": "2026-01-09T10:30:00Z",
  "updated_at": "2026-01-09T10:30:00Z"
}
```