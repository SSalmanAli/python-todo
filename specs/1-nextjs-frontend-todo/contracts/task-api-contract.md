# API Contract: Task Management Endpoints

## Overview
API contract for the task management functionality that the Next.js frontend will consume from the FastAPI backend.

## Authentication
All endpoints require JWT token authentication in the Authorization header:
```
Authorization: Bearer <JWT_TOKEN>
```

## Base URL
`${BACKEND_API_URL}/api/v1`

## Endpoints

### GET /tasks
**Description**: Retrieve all tasks for the authenticated user

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Query Parameters**:
- `limit` (optional): Maximum number of tasks to return
- `offset` (optional): Number of tasks to skip (for pagination)

**Response**:
- Status: `200 OK`
- Body:
```json
{
  "tasks": [
    {
      "id": "string",
      "userId": "string",
      "title": "string",
      "description": "string (optional)",
      "completed": false,
      "createdAt": "ISO 8601 timestamp",
      "updatedAt": "ISO 8601 timestamp"
    }
  ]
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `403 Forbidden`: User attempting to access another user's tasks

---

### POST /tasks
**Description**: Create a new task for the authenticated user

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "title": "string (required)",
  "description": "string (optional)"
}
```

**Response**:
- Status: `201 Created`
- Body:
```json
{
  "id": "string",
  "userId": "string",
  "title": "string",
  "description": "string (optional)",
  "completed": false,
  "createdAt": "ISO 8601 timestamp",
  "updatedAt": "ISO 8601 timestamp"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid request body (missing title, etc.)
- `401 Unauthorized`: Invalid or missing JWT token
- `422 Unprocessable Entity`: Validation error

---

### GET /tasks/{id}
**Description**: Retrieve a specific task by ID

**Path Parameters**:
- `id`: Task ID (string)

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Response**:
- Status: `200 OK`
- Body:
```json
{
  "id": "string",
  "userId": "string",
  "title": "string",
  "description": "string (optional)",
  "completed": false,
  "createdAt": "ISO 8601 timestamp",
  "updatedAt": "ISO 8601 timestamp"
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `403 Forbidden`: User attempting to access another user's task
- `404 Not Found`: Task with given ID does not exist

---

### PUT /tasks/{id}
**Description**: Update an existing task

**Path Parameters**:
- `id`: Task ID (string)

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`
- `Content-Type: application/json`

**Request Body**:
```json
{
  "title": "string (optional)",
  "description": "string (optional)",
  "completed": "boolean (optional)"
}
```

**Response**:
- Status: `200 OK`
- Body:
```json
{
  "id": "string",
  "userId": "string",
  "title": "string",
  "description": "string (optional)",
  "completed": "boolean",
  "createdAt": "ISO 8601 timestamp",
  "updatedAt": "ISO 8601 timestamp"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid request body
- `401 Unauthorized`: Invalid or missing JWT token
- `403 Forbidden`: User attempting to update another user's task
- `404 Not Found`: Task with given ID does not exist

---

### DELETE /tasks/{id}
**Description**: Delete a specific task

**Path Parameters**:
- `id`: Task ID (string)

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Response**:
- Status: `204 No Content`

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `403 Forbidden`: User attempting to delete another user's task
- `404 Not Found`: Task with given ID does not exist

---

### PATCH /tasks/{id}/toggle
**Description**: Toggle the completion status of a task

**Path Parameters**:
- `id`: Task ID (string)

**Headers**:
- `Authorization: Bearer <JWT_TOKEN>`

**Response**:
- Status: `200 OK`
- Body:
```json
{
  "id": "string",
  "userId": "string",
  "title": "string",
  "description": "string (optional)",
  "completed": "boolean",
  "createdAt": "ISO 8601 timestamp",
  "updatedAt": "ISO 8601 timestamp"
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing JWT token
- `403 Forbidden`: User attempting to toggle another user's task
- `404 Not Found`: Task with given ID does not exist