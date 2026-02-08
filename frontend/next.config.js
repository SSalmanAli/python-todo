/** @type {import('next').NextConfig} */
const nextConfig = {
  env: {
    NEXTAUTH_URL: process.env.NEXTAUTH_URL || 'http://localhost:3000',
    NEXTAUTH_SECRET: process.env.NEXTAUTH_SECRET || 'your-secret-key-here',
    BACKEND_API_URL: process.env.BACKEND_API_URL || 'https://salman-12-python-todo-backend.hf.space/',
    BACKEND_API_BASE_PATH: process.env.BACKEND_API_BASE_PATH || '/api/v1',
  }
};

module.exports = nextConfig;