import { withAuth } from 'next-auth/middleware';
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  // Allow access to auth pages without authentication
  if (request.nextUrl.pathname.startsWith('/auth')) {
    return NextResponse.next();
  }

  // For other routes (including root), require authentication
  return withAuth({
    pages: {
      signIn: '/auth/login',
    },
  })(request);
}

// Apply middleware to all routes except auth pages
export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico|auth).*)'],
};