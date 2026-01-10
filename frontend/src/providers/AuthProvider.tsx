// Authentication context/provider for managing user session state

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { UserSession } from '../types/auth.types';

interface AuthContextType {
  userSession: UserSession | null;
  login: (token: string, userId: string) => void;
  logout: () => void;
  isAuthenticated: boolean;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [userSession, setUserSession] = useState<UserSession | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Check for existing session on component mount
    const storedToken = localStorage.getItem('authToken');
    const storedUserId = localStorage.getItem('userId');

    if (storedToken && storedUserId) {
      const session: UserSession = {
        userId: storedUserId,
        token: storedToken,
        expiresAt: localStorage.getItem('expiresAt') || '',
        isAuthenticated: true,
      };
      setUserSession(session);
    }

    setIsLoading(false);
  }, []);

  const login = (token: string, userId: string) => {
    const session: UserSession = {
      userId,
      token,
      expiresAt: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(), // 24 hours from now
      isAuthenticated: true,
    };

    setUserSession(session);

    // Store in localStorage
    localStorage.setItem('authToken', token);
    localStorage.setItem('userId', userId);
    localStorage.setItem('expiresAt', session.expiresAt);
  };

  const logout = () => {
    setUserSession(null);

    // Remove from localStorage
    localStorage.removeItem('authToken');
    localStorage.removeItem('userId');
    localStorage.removeItem('expiresAt');
  };

  const value: AuthContextType = {
    userSession,
    login,
    logout,
    isAuthenticated: !!userSession?.isAuthenticated,
    isLoading,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};