'use client';

import React, { useState, useEffect } from 'react';
import TaskList from '@/components/tasks/TaskList';
import TaskForm from '@/components/tasks/TaskForm';
import { Task } from '@/lib/types/task.types';
import { apiClient } from '@/lib/api/client';
import { useAuth } from '@/providers/AuthProvider';

const DashboardPage = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    if (isAuthenticated) {
      fetchTasks();
    }
  }, [isAuthenticated]);

  const fetchTasks = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await apiClient.getTasks();
      if (response.success) {
        setTasks(response.data || []);
      } else {
        setError(response.error?.message || 'Failed to fetch tasks');
      }
    } catch (err: any) {
      setError(err.message || 'An error occurred while fetching tasks');
    } finally {
      setLoading(false);
    }
  };

  const handleTaskCreated = () => {
    fetchTasks(); // Refresh the task list
  };

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-md w-full space-y-8">
          <div className="text-center">
            <h2 className="text-2xl font-bold text-gray-800">Access Denied</h2>
            <p className="mt-2 text-gray-600">Please log in to access this page.</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Your Todo Dashboard</h1>
        <p className="mt-2 text-gray-600">Manage your tasks efficiently</p>
      </div>

      <div className="mb-8">
        <TaskForm onTaskCreated={handleTaskCreated} />
      </div>

      {error && (
        <div className="mb-4 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span className="block sm:inline">{error}</span>
        </div>
      )}

      <div>
        <h2 className="text-xl font-semibold text-gray-800 mb-4">Your Tasks</h2>
        {loading ? (
          <div className="flex justify-center items-center h-32">
            <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-indigo-500"></div>
          </div>
        ) : (
          <TaskList initialTasks={tasks} />
        )}
      </div>
    </div>
  );
};

export default DashboardPage;