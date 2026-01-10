# Quickstart Guide: Next.js Frontend Todo Application

## Prerequisites
- Node.js 18.x or higher
- npm or yarn package manager
- Access to the FastAPI backend service
- BetterAuth configuration details

## Setup Instructions

### 1. Clone and Initialize
```bash
# Clone the repository
git clone <repository-url>
cd frontend

# Install dependencies
npm install
# or
yarn install
```

### 2. Environment Configuration
Copy the environment template and configure your settings:

```bash
cp .env.example .env.local
```

Edit `.env.local` with your configuration:
```env
# Backend API Configuration
BACKEND_API_URL=http://localhost:8000  # URL of your FastAPI backend
BACKEND_API_BASE_PATH=/api/v1          # Base path for API endpoints

# BetterAuth Configuration
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
BETTER_AUTH_SECRET=your-secret-key-here
BETTER_AUTH_TRUST_HOST=true

# Additional environment variables as needed
```

### 3. Run the Development Server
```bash
npm run dev
# or
yarn dev
```

Visit `http://localhost:3000` to access the application.

## Key Features

### Authentication
- User login/logout functionality using BetterAuth
- Automatic JWT token management
- Protected routes that require authentication

### Task Management
- View all tasks assigned to the authenticated user
- Create new tasks with title and description
- Update existing tasks
- Delete tasks
- Toggle task completion status

### API Integration
- Centralized API client in `lib/api/client.ts`
- Automatic JWT token attachment to requests
- Error handling and loading states

## Project Structure
```
src/
├── app/                    # Next.js App Router pages
│   ├── (auth)/            # Authentication pages
│   ├── dashboard/         # Main task dashboard
│   └── layout.tsx         # Root layout
├── components/            # Reusable UI components
│   ├── auth/              # Authentication components
│   └── tasks/             # Task management components
├── lib/                   # Utilities and helpers
│   ├── api/               # API client and utilities
│   └── auth/              # Authentication helpers
├── hooks/                 # Custom React hooks
└── providers/             # React context providers
```

## Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npm run test` - Run tests

## Environment Variables
- `BACKEND_API_URL` - Base URL for the FastAPI backend
- `NEXT_PUBLIC_BETTER_AUTH_URL` - BetterAuth server URL
- `BETTER_AUTH_SECRET` - Secret key for authentication