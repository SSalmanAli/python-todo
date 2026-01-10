# Research & Discovery: Next.js Frontend Todo Application

## Overview
Research and discovery for implementing a Next.js frontend application that consumes an existing FastAPI backend for todo management with BetterAuth authentication.

## Technology Decisions

### Next.js with App Router
**Decision**: Use Next.js 14+ with App Router for the frontend framework
**Rationale**:
- Modern React framework with excellent developer experience
- Built-in routing with App Router for better code organization
- Server-side rendering and static generation capabilities
- Strong TypeScript support
- Large ecosystem and community support
- Perfect for consuming external APIs

**Alternatives considered**:
- React + Vite + React Router: More manual setup required
- Vue.js/Nuxt: Different ecosystem, less familiarity
- Angular: Heavier framework, steeper learning curve

### BetterAuth for Authentication
**Decision**: Use BetterAuth for authentication management
**Rationale**:
- Lightweight and flexible authentication library
- Designed for modern frameworks like Next.js
- Handles JWT token management
- Easy integration with various providers
- Good security practices out of the box
- Fits well with the requirement to consume existing backend

**Alternatives considered**:
- NextAuth.js: Popular but primarily designed for Next.js Pages Router
- Clerk: More heavy-handed, opinionated approach
- Auth0/Firebase: Third-party services, more complexity

### API Client Strategy
**Decision**: Implement centralized API client with automatic JWT token attachment
**Rationale**:
- Centralizes all API communication in one place
- Ensures consistent JWT token handling across the application
- Makes error handling and request/response interception easier
- Simplifies testing and maintenance
- Aligns with clean architecture principles

**Alternatives considered**:
- Direct fetch calls: Would lead to code duplication and inconsistent handling
- Multiple client instances: Would complicate token management

### Styling Approach
**Decision**: Use Tailwind CSS for styling
**Rationale**:
- Utility-first CSS framework for rapid development
- Excellent integration with React/Next.js
- Responsive design capabilities out of the box
- Customizable and themeable
- Small bundle size when properly configured

**Alternatives considered**:
- Styled-components: Runtime overhead
- Traditional CSS: More verbose, harder to maintain consistency
- Material UI: Too opinionated for this simple application

### State Management
**Decision**: Use React Context API with custom hooks for global state
**Rationale**:
- Light-weight solution for this application size
- Built into React, no additional dependencies
- Good for authentication state and simple app-wide state
- Can be extended with Zustand if needed later

**Alternatives considered**:
- Redux Toolkit: Overkill for this simple application
- Zustand: Good alternative but Context API sufficient initially

## API Contract Understanding

Based on the backend constitution, the FastAPI backend provides these endpoints:
- GET /tasks (list tasks for authenticated user)
- POST /tasks (create task)
- GET /tasks/{id} (retrieve task details)
- PUT /tasks/{id} (update task)
- DELETE /tasks/{id} (delete task)
- PATCH /tasks/{id}/toggle (toggle completion status)

The frontend needs to:
- Attach JWT tokens to all authenticated requests
- Handle user_id scoping automatically
- Handle proper error responses from backend
- Manage loading and error states consistently

## Authentication Flow

BetterAuth integration will involve:
- Setting up BetterAuth client-side
- Implementing login/register flows
- Storing and managing JWT tokens
- Intercepting API requests to attach tokens
- Handling token refresh/expiration
- Redirecting users based on authentication state