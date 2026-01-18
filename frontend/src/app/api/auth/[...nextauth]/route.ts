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
          // Simulate API call to backend for authentication
          // This is a mock implementation - replace with actual backend call
          try {
            // In a real implementation, you would make a call to your FastAPI backend
            const response = await fetch(`${process.env.BACKEND_API_URL}/api/v1/auth/login`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                email: credentials.email,
                password: credentials.password
              })
            });

            if (!response.ok) {
              throw new Error('Invalid credentials');
            }

            const user = await response.json();
            return {
              id: user.id,
              name: user.name,
              email: user.email,
              accessToken: user.accessToken
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