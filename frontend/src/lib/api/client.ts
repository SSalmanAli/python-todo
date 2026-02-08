// Centralized API client with JWT token attachment

import { Task, CreateTaskRequest, UpdateTaskRequest, ApiResponse } from '../types/task.types';
import { snakeToCamel } from '../utils/transform';

const BACKEND_API_URL = process.env.BACKEND_API_URL || 'http://localhost:8000';

class ApiClient {
  private baseUrl: string;

  constructor() {
    this.baseUrl = `${BACKEND_API_URL}`;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<ApiResponse<T>> {
    try {
      // Get the JWT token from wherever it's stored (e.g., localStorage, context)
      // For now, we'll get it from localStorage which is set by our AuthProvider
      const token = this.getAuthToken();

      const headers = {
        'Content-Type': 'application/json',
        ...options.headers,
      } as Record<string, string>;

      if (token) {
        headers['Authorization'] = `Bearer ${token}`;
      }

      const response = await fetch(`${this.baseUrl}${endpoint}`, {
        ...options,
        headers,
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        return {
          success: false,
          error: {
            message: errorData.message || `HTTP error! status: ${response.status}`,
            code: response.status.toString(),
            details: errorData,
          },
        };
      }

      // Handle responses that may not have a body (e.g., 204 No Content)
      let data = undefined;

      // Check if response has content
      if (response.status !== 204 && response.headers.get('content-length') !== '0') {
        const contentType = response.headers.get('content-type');

        if (contentType && contentType.includes('application/json')) {
          const rawData = await response.json();
          // Transform snake_case response to camelCase for frontend
          data = snakeToCamel(rawData);
        } else {
          // For non-JSON responses, get text content
          data = await response.text();
        }
      }

      return {
        success: true,
        data,
      };
    } catch (error: any) {
      return {
        success: false,
        error: {
          message: error.message || 'Network error occurred',
          code: 'NETWORK_ERROR',
          details: error,
        },
      };
    }
  }

  private getAuthToken(): string | null {
    // Get the token from localStorage where AuthProvider stores it
    if (typeof window !== 'undefined') {
      return localStorage.getItem('authToken') || localStorage.getItem('next-auth.session-token');
    }
    return null;
  }

  // Task-related API methods
  async getTasks(): Promise<ApiResponse<Task[]>> {
    return this.request<Task[]>('/tasks/');
  }

  async createTask(taskData: CreateTaskRequest): Promise<ApiResponse<Task>> {
    return this.request<Task>('/tasks/', {
      method: 'POST',
      body: JSON.stringify(taskData),
    });
  }

  async getTaskById(id: string): Promise<ApiResponse<Task>> {
    return this.request<Task>(`/tasks/${id}`);
  }

  async updateTask(id: string, taskData: UpdateTaskRequest): Promise<ApiResponse<Task>> {
    return this.request<Task>(`/tasks/${id}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  }

  async deleteTask(id: string): Promise<ApiResponse<void>> {
    return this.request<void>(`/tasks/${id}`, {
      method: 'DELETE',
    });
  }

  async toggleTaskCompletion(id: string): Promise<ApiResponse<Task>> {
    return this.request<Task>(`/tasks/${id}/toggle`, {
      method: 'PATCH',
    });
  }
}

export const apiClient = new ApiClient();