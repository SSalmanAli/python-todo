// TypeScript types for Task entity

export interface Task {
  id: string;              // Unique identifier for the task
  userId: string;          // User ID to scope tasks to specific user
  title: string;           // Required task title
  description?: string;    // Optional task description
  completed: boolean;      // Boolean indicating completion status
  createdAt: string;       // ISO 8601 timestamp when task was created
  updatedAt: string;       // ISO 8601 timestamp when task was last updated
}

export interface CreateTaskRequest {
  title: string;
  description?: string;
}

export interface UpdateTaskRequest {
  title?: string;
  description?: string;
  completed?: boolean;
}

export interface ApiResponse<T> {
  data?: T;
  error?: {
    message: string;
    code: string;
    details?: any;
  };
  success: boolean;
}