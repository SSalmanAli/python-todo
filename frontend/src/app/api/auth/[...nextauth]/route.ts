import NextAuth from 'next-auth';
import CredentialsProvider from 'next-auth/providers/credentials';
import { JWT } from 'next-auth/jwt';

// Define the auth options for NextAuth
const authOptions = {
  providers: [
    CredentialsProvider({
      name: 'Credentials',
      credentials: {
        email: { label: "Email", type: "email", placeholder: "email@example.com" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials: any) {
        // This is where you would typically call your backend API to authenticate the user
        // For now, we'll simulate authentication with mock data
        // In a real implementation, you would call your FastAPI backend

        if (credentials?.email && credentials?.password) {
          // Call the FastAPI backend for authentication
          try {
            const response = await fetch(`${process.env.BACKEND_API_URL}/auth/token`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                email: credentials.email,
                password: credentials.password
              })
            });

            if (!response.ok) {
              // Log the error details for debugging
              const errorData = await response.json().catch(() => ({}));
              console.error('Authentication error response:', errorData);
              throw new Error(`Invalid credentials: ${response.status}`);
            }

            const tokenData = await response.json();

            // Get user details using the token
            const userResponse = await fetch(`${process.env.BACKEND_API_URL}/auth/me`, {
              headers: {
                'Authorization': `Bearer ${tokenData.access_token}`
              }
            });

            if (!userResponse.ok) {
              throw new Error('Failed to fetch user details');
            }

            const userData = await userResponse.json();

            return {
              id: userData.id,
              name: userData.username,
              email: userData.email,
              accessToken: tokenData.access_token
            };
          } catch (error) {
            console.error('Authentication error:', error);
          }
        }

        // Return null if authentication fails
        return null;
      }
    })
  ],
  callbacks: {
    async jwt({ token, user }: { token: JWT, user?: any }) {
      if (user) {
        token.accessToken = user.accessToken;
        token.id = user.id;
      }
      return token;
    },
    async session({ session, token }: { session: any, token: JWT }) {
      if (token) {
        session.user.id = token.id;
        session.accessToken = token.accessToken as string;
      }
      return session;
    }
  },
  pages: {
    signIn: '/auth/login',
  },
  session: {
    strategy: 'jwt' as const,
    maxAge: 24 * 60 * 60, // 24 hours
  },
  secret: process.env.NEXTAUTH_SECRET || 'your-secret-key-here',
};

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };

// Export config to allow all routes in this file
export const dynamic = 'force-dynamic';