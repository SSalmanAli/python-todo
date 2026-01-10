# Quickstart Guide: FastAPI Todo Backend Service

## Prerequisites

- Python 3.11+
- pip package manager
- Virtual environment tool (venv or conda)
- Access to NeonDB (PostgreSQL) instance

## Setup Instructions

### 1. Clone and Navigate
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

For development:
```bash
pip install -r requirements-dev.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
DATABASE_URL=postgresql+asyncpg://username:password@neondb-host.region.neon.tech/dbname
SECRET_KEY=your-super-secret-jwt-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Database Setup
```bash
# Initialize database tables
python -m src.config.database init

# Or run migrations
alembic upgrade head
```

### 6. Run the Application
```bash
# Development
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Production
gunicorn src.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## API Endpoints

### Authentication
All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <jwt-token>
```

### Available Endpoints

#### Tasks Management
- `GET /tasks` - List all tasks for authenticated user
- `POST /tasks` - Create a new task
- `GET /tasks/{id}` - Get specific task details
- `PUT /tasks/{id}` - Update entire task
- `DELETE /tasks/{id}` - Delete a task
- `PATCH /tasks/{id}/toggle` - Toggle completion status

## Testing

### Run Unit Tests
```bash
pytest tests/unit/
```

### Run Integration Tests
```bash
pytest tests/integration/
```

### Run All Tests
```bash
pytest tests/
```

## Project Structure
```
backend/
├── src/
│   ├── main.py                 # Application entry point
│   ├── config/
│   │   ├── database.py         # Database setup
│   │   ├── security.py         # JWT handling
│   │   └── settings.py         # Configuration
│   ├── models/
│   │   └── task.py             # SQLModel definitions
│   ├── schemas/
│   │   └── task.py             # Pydantic schemas
│   ├── services/
│   │   └── task_service.py     # Business logic
│   └── api/
│       └── routes/
│           └── tasks.py        # API endpoints
├── tests/
│   ├── test_main.py
│   ├── test_task_models.py
│   ├── test_task_service.py
│   └── test_task_routes.py
├── requirements.txt
├── requirements-dev.txt
└── alembic/
    └── versions/
```

## Development Commands

### Format Code
```bash
black src/ tests/
```

### Lint Code
```bash
flake8 src/ tests/
```

### Type Check
```bash
mypy src/
```

## Troubleshooting

### Common Issues
- **Database Connection**: Verify DATABASE_URL in environment variables
- **JWT Errors**: Check SECRET_KEY and algorithm settings
- **Migration Issues**: Run `alembic upgrade head` to sync database
- **Import Errors**: Activate virtual environment and reinstall dependencies

### Health Check
Visit `http://localhost:8000/health` to verify the application is running