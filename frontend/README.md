# Next.js Frontend Todo Application

This is the frontend for the Todo application built with Next.js, TypeScript, and Tailwind CSS. It consumes the FastAPI backend for all data operations and uses BetterAuth for authentication.

## Features

- User authentication and authorization
- Create, read, update, and delete tasks
- Toggle task completion status
- Responsive design for desktop and mobile
- Loading and error states
- JWT token management

## Prerequisites

- Node.js 18.x or higher
- Access to the FastAPI backend service

## Installation

1. Clone the repository
2. Navigate to the frontend directory: `cd frontend`
3. Install dependencies: `npm install`
4. Copy the environment file: `cp .env.example .env.local`
5. Update the environment variables with your backend configuration

## Environment Variables

- `BACKEND_API_URL`: Base URL for the FastAPI backend (default: http://localhost:8000)
- `BACKEND_API_BASE_PATH`: Base path for API endpoints (default: /api/v1)
- `NEXT_PUBLIC_BETTER_AUTH_URL`: BetterAuth server URL
- `BETTER_AUTH_SECRET`: Secret key for authentication

## Running the Application

- Development: `npm run dev`
- Production build: `npm run build`
- Production server: `npm run start`
- Linting: `npm run lint`

## Project Structure

```
frontend/
├── src/
│   ├── app/                    # Next.js App Router pages
│   │   ├── (auth)/            # Authentication-related pages
│   │   │   ├── login/
│   │   │   └── register/
│   │   ├── dashboard/         # Main dashboard with tasks
│   │   ├── globals.css        # Global styles
│   │   └── layout.tsx         # Root layout
│   ├── components/            # Reusable UI components
│   │   ├── auth/              # Authentication components
│   │   └── tasks/             # Task management components
│   ├── lib/                   # Utilities and helper functions
│   │   ├── api/               # API client and request utilities
│   │   └── types/             # TypeScript type definitions
│   ├── hooks/                 # Custom React hooks
│   └── providers/             # React context providers
├── public/                    # Static assets
├── .env.example              # Environment variables template
├── next.config.js            # Next.js configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── tsconfig.json             # TypeScript configuration
└── package.json              # Dependencies and scripts
```

## API Integration

The application uses a centralized API client that automatically attaches JWT tokens to all authenticated requests. All communication with the backend follows the API contracts defined in the project documentation.