# Next.js Frontend Todo Application

This is the frontend for the Todo application built with Next.js, TypeScript, Tailwind CSS, and NextAuth. It consumes the FastAPI backend for all data operations and uses NextAuth for authentication.

## Features

- User authentication and authorization with NextAuth
- Create, read, update, and delete tasks
- Toggle task completion status
- Responsive design for desktop and mobile
- Loading and error states
- JWT token management

## Prerequisites

- Node.js 18.x or higher
- Access to the FastAPI backend service

## Installation

1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies: `npm install`
3. Copy the environment file: `cp .env.example .env.local`
4. Update the environment variables with your backend configuration

## Environment Variables

Create a `.env.local` file with the following variables:

```env
# Backend API Configuration
BACKEND_API_URL=http://localhost:8000
BACKEND_API_BASE_PATH=/api/v1

# NextAuth Configuration
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your-secret-key-here
```

## Running the Application

- Development: `npm run dev`
- Production build: `npm run build`
- Production server: `npm run start`
- Linting: `npm run lint`

## Authentication

The application uses NextAuth for authentication with a credentials provider. For testing purposes, you can use:
- Email: `user@example.com`
- Password: `password`

## Project Structure

```
frontend/
├── src/
│   ├── app/                    # Next.js App Router pages
│   │   ├── api/               # API routes (including NextAuth)
│   │   │   └── auth/[...nextauth]/ # NextAuth API route
│   │   ├── auth/              # Authentication-related pages
│   │   │   └── login/         # Login page
│   │   ├── dashboard/         # Main dashboard with tasks
│   │   ├── globals.css        # Global styles
│   │   └── layout.tsx         # Root layout
│   ├── components/            # Reusable UI components
│   │   ├── auth/              # Authentication components
│   │   └── tasks/             # Task management components
│   ├── lib/                   # Utilities and helper functions
│   │   ├── api/               # API client and request utilities
│   │   └── types/             # TypeScript type definitions
│   ├── providers/             # React context providers
│   └── auth/                  # NextAuth configuration
├── public/                    # Static assets
├── .env.example              # Environment variables template
├── next.config.js            # Next.js configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── tsconfig.json             # TypeScript configuration
└── package.json              # Dependencies and scripts
```

## API Integration

The application uses a centralized API client that automatically attaches JWT tokens to all authenticated requests. All communication with the backend follows the API contracts defined in the project documentation.