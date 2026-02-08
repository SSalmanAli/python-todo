// TypeScript types for UserSession entity

export interface UserSession {
  userId: string;          // User identifier from authentication
  token: string;           // JWT token for API authentication
  expiresAt: string;       // ISO 8601 timestamp, expiration of the token
  isAuthenticated: boolean; // Whether the user is currently authenticated
}