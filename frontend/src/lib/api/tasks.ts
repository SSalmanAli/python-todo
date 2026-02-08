// Task-specific API functions
// These are already implemented in the main API client, but we can create a separate module
// to organize task-specific functions if needed

import { apiClient } from './client';
import { Task, CreateTaskRequest, UpdateTaskRequest, ApiResponse } from '../types/task.types';

// Export the task-related methods from the main client for convenience
export const taskApi = {
  getTasks: (): Promise<ApiResponse<Task[]>> => {
    return apiClient.getTasks();
  },

  createTask: (taskData: CreateTaskRequest): Promise<ApiResponse<Task>> => {
    return apiClient.createTask(taskData);
  },

  getTaskById: (id: string): Promise<ApiResponse<Task>> => {
    return apiClient.getTaskById(id);
  },

  updateTask: (id: string, taskData: UpdateTaskRequest): Promise<ApiResponse<Task>> => {
    return apiClient.updateTask(id, taskData);
  },

  deleteTask: (id: string): Promise<ApiResponse<void>> => {
    return apiClient.deleteTask(id);
  },

  toggleTaskCompletion: (id: string): Promise<ApiResponse<Task>> => {
    return apiClient.toggleTaskCompletion(id);
  }
};