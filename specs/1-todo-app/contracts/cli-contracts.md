# CLI Contracts: Python In-Memory Console Todo App

## Command Interface Specification

### Add Command
- **Signature**: `add --title <title> [--description <description>]`
- **Input**:
  - Required: `title` (string, non-empty)
  - Optional: `description` (string)
- **Output**: Success message with assigned task ID
- **Error Cases**:
  - Title is empty → Error message
  - Invalid arguments → Usage help

### List Command
- **Signature**: `list`
- **Input**: None
- **Output**: Formatted list of all tasks with ID, title, description, and status
- **Error Cases**: None

### Update Command
- **Signature**: `update --id <id> [--title <title>] [--description <description>]`
- **Input**:
  - Required: `id` (integer, valid task ID)
  - Optional: `title` (string), `description` (string)
- **Output**: Success confirmation
- **Error Cases**:
  - Task ID doesn't exist → Error message
  - Invalid arguments → Usage help

### Delete Command
- **Signature**: `delete --id <id>`
- **Input**:
  - Required: `id` (integer, valid task ID)
- **Output**: Success confirmation
- **Error Cases**:
  - Task ID doesn't exist → Error message
  - Invalid arguments → Usage help

### Mark Command
- **Signature**: `mark --id <id> --status <status>`
- **Input**:
  - Required: `id` (integer, valid task ID), `status` (enum: "complete" or "incomplete")
- **Output**: Success confirmation
- **Error Cases**:
  - Task ID doesn't exist → Error message
  - Invalid status → Error message
  - Invalid arguments → Usage help

## Data Contracts

### Task Representation
```
{
  "id": integer,
  "title": string,
  "description": string | null,
  "completed": boolean
}
```

### Response Format
- **Success**: Human-readable message confirming operation
- **Error**: Human-readable error message prefixed with "Error:"