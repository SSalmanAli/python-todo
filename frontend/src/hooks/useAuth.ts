// Custom authentication hook - This is a placeholder since we already have useAuth in AuthProvider
// In a real implementation, this would be part of the AuthProvider file or would import from there
// For now, we'll create a simple utility file that can be used to manage auth state

import { useState, useEffect } from 'react';

// This hook provides authentication utilities that can be used across the app
export const useAuthUtilities = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Check if user is authenticated by checking for token in storage
    const token = localStorage.getItem('authToken');
    setIsAuthenticated(!!token);
    setIsLoading(false);
  }, []);

  const login = (token: string, userId: string) => {
    localStorage.setItem('authToken', token);
    localStorage.setItem('userId', userId);
    setIsAuthenticated(true);
  };

  const logout = () => {
    localStorage.removeItem('authToken');
    localStorage.removeItem('userId');
    localStorage.removeItem('expiresAt');
    setIsAuthenticated(false);
  };

  const getAuthToken = (): string | null => {
    return localStorage.getItem('authToken');
  };

  return {
    isAuthenticated,
    isLoading,
    login,
    logout,
    getAuthToken,
  };
};

// Note: The actual useAuth hook is already defined in AuthProvider.tsx
// This is just an additional utility hook for auth-related functions