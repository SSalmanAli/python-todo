'use client';

import React, { useState } from 'react';
import { Task } from '@/lib/types/task.types';
import { apiClient } from '@/lib/api/client';

interface TaskCardProps {
  task: Task;
  onUpdate: () => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onUpdate }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description || '');
  const [error, setError] = useState<string | null>(null);

  const handleToggleComplete = async () => {
    try {
      const response = await apiClient.toggleTaskCompletion(task.id);
      if (response.success) {
        onUpdate(); // Refresh the task list
      } else {
        setError(response.error?.message || 'Failed to update task');
      }
    } catch (err: any) {
      setError(err.message || 'An error occurred while updating the task');
    }
  };

  const handleDelete = async () => {
    if (window.confirm(`Are you sure you want to delete "${task.title}"?`)) {
      try {
        const response = await apiClient.deleteTask(task.id);
        if (response.success) {
          onUpdate(); // Refresh the task list
        } else {
          setError(response.error?.message || 'Failed to delete task');
        }
      } catch (err: any) {
        setError(err.message || 'An error occurred while deleting the task');
      }
    }
  };

  const handleSaveEdit = async () => {
    try {
      const response = await apiClient.updateTask(task.id, {
        title,
        description,
      });
      if (response.success) {
        setIsEditing(false);
        onUpdate(); // Refresh the task list
      } else {
        setError(response.error?.message || 'Failed to update task');
      }
    } catch (err: any) {
      setError(err.message || 'An error occurred while updating the task');
    }
  };

  const handleCancelEdit = () => {
    setIsEditing(false);
    // Reset to original values
    setTitle(task.title);
    setDescription(task.description || '');
  };

  return (
    <div className={`border rounded-lg p-4 shadow-sm ${task.completed ? 'bg-green-50' : 'bg-white'}`}>
      {error && (
        <div className="mb-2 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span className="block sm:inline">{error}</span>
        </div>
      )}

      {isEditing ? (
        <div className="space-y-3">
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full p-2 border rounded-md mb-2"
            placeholder="Task title"
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full p-2 border rounded-md mb-2"
            placeholder="Task description"
            rows={3}
          />
          <div className="flex space-x-2">
            <button
              onClick={handleSaveEdit}
              className="px-3 py-1 bg-green-600 text-white rounded-md text-sm"
            >
              Save
            </button>
            <button
              onClick={handleCancelEdit}
              className="px-3 py-1 bg-gray-500 text-white rounded-md text-sm"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : (
        <div>
          <div className="flex items-start">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={handleToggleComplete}
              className="mt-1 mr-3 h-5 w-5 text-indigo-600 rounded"
            />
            <div className="flex-1">
              <h3 className={`text-lg font-medium ${task.completed ? 'line-through text-gray-500' : 'text-gray-900'}`}>
                {task.title}
              </h3>
              {task.description && (
                <p className={`mt-1 ${task.completed ? 'line-through text-gray-500' : 'text-gray-600'}`}>
                  {task.description}
                </p>
              )}
              <div className="mt-2 text-xs text-gray-500">
                Created: {new Date(task.createdAt).toLocaleDateString()}
                {task.updatedAt !== task.createdAt && ` | Updated: ${new Date(task.updatedAt).toLocaleDateString()}`}
              </div>
            </div>
          </div>
          <div className="mt-3 flex space-x-2">
            <button
              onClick={() => setIsEditing(true)}
              className="px-3 py-1 bg-blue-600 text-white rounded-md text-sm"
            >
              Edit
            </button>
            <button
              onClick={handleDelete}
              className="px-3 py-1 bg-red-600 text-white rounded-md text-sm"
            >
              Delete
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskCard;