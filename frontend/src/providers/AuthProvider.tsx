"use client";

// Authentication context/provider using NextAuth
import React, { createContext, useContext, ReactNode, useEffect, useState } from 'react';
import { useSession, signIn, signOut } from 'next-auth/react';
import { UserSession } from '@/lib/types/auth.types';

interface AuthContextType {
  userSession: UserSession | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  isAuthenticated: boolean;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const { data: session, status } = useSession();
  const [userSession, setUserSession] = useState<UserSession | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (status === 'loading') {
      setIsLoading(true);
    } else {
      setIsLoading(false);
      if (session && session.user) {
        const nextAuthUserSession: UserSession = {
          userId: (session as any).user?.id || '',
          token: (session as any).accessToken || '',
          expiresAt: session.expires || '',
          isAuthenticated: true,
        };
        setUserSession(nextAuthUserSession);

        // Store token in localStorage for API client
        if ((session as any).accessToken) {
          localStorage.setItem('authToken', (session as any).accessToken);
        }
      } else {
        setUserSession(null);
        localStorage.removeItem('authToken');
      }
    }
  }, [session, status]);

  const login = async (email: string, password: string) => {
    try {
      const result = await signIn('credentials', {
        email,
        password,
        redirect: false,
      });

      if (result?.error) {
        throw new Error(result.error);
      }
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  };

  const logout = async () => {
    await signOut({ redirect: false });
  };

  const value: AuthContextType = {
    userSession,
    login,
    logout,
    isAuthenticated: !!session,
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