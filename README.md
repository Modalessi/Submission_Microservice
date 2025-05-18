# Submission Microservice

This is a Submission Microservice for a "Backend Take-Home Task" that provides a REST API for handling code submissions, evaluations, and retrieving results.

## Project Overview

This lightweight backend service supports a coding platform by:
1. Accepting user code submissions
2. Processing submissions asynchronously
3. Simulating evaluations with random results
4. Providing endpoints to query submission status and history

## Functional Requirements (All Completed)

1. **Submit a Solution** - `POST /submissions`
   - Request body: 
     ```json
     { 
       "user_id": "string", 
       "problem_id": "string", 
       "language": "string", 
       "source_code": "string" 
     }
     ```
   - Response: 
     ```json
     { 
       "submission_id": "string", 
       "status": "pending" 
     }
     ```

2. **View Submission Status** - `GET /submissions/{submission_id}`
   - Returns submission details:
  ```json
  {
        "user_id": "str",
        "problem_id": "str",
        "language": "str",
        "source_code": "str",
        "status": "str",
        "result": "str",
        "execution_time": 0
    }
  ```

3. **Simulated Evaluation Job**
   - Asynchronous process that:
     - Waits a few seconds
     - Updates submission with random result (Accepted, Wrong Answer, TLE, etc.)
     - Adds random execution time

4. **List User Submissions** - `GET /users/{user_id}/submissions`
   - Returns array of all submissions for a user, sorted by latest

## Technical Implementation

1. **Framework & Database**
   - FastAPI with SQLModel ORM
   - PostgreSQL database for persistent storage

2. **Authentication**
   - JWT-based authentication for secure API access
   - User registration and login endpoints

3. **Async Task Handling**
   - Background tasks for submission evaluation
   - Asynchronous updating of submission status

4. **Rate Limiting**
   - Redis-based rate limiting (max 5 submissions per minute per user)
   - Protection against API abuse


## API Endpoints

| Endpoint | Method | Description | Authentication |
|----------|--------|-------------|---------------|
| `/health` | GET | Health check endpoint | No |
| `/users/register` | POST | Register new user | No |
| `/users/login` | POST | Login and get JWT token | No |
| `/submissions` | POST | Submit a solution | Yes |
| `/submissions/{submission_id}` | GET | Get submission details | No |
| `/users/{user_id}/submissions` | GET | List all user submissions | No |

## Setup and Installation

### Prerequisites
- Docker and Docker Compose
- Python 3.9+

### Environment Variables
Create a `.env` file with the following:
```
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
redis_url=r
rate_limit=
time_window=
# JWT settings
jwt_secret=
jwt_algorithm=
jwt_access_token_expire_minutes=
```

### Running with Docker
```bash
docker-compose up -d
```

### Technical Decisions

This app architecture is thin, there is not much abstraction.  
For simplicity and flexibility.

All the routes are in `main.py`, normally I would split these routes into their own files and use `APIRouter()`, and join them in the main.

But there are few routes here, so I decided putting them all in the main is okay.

##### Services  
All the things this backend can do, and accessed by the routes directly.

I don’t like using service classes and so on, I think of them as an unnecessary layer of abstraction.

But in a big project I will split them using entities and make each entity have its own routes, models, and services.

This makes it much simpler imo.

##### Auth  
I used straightforward JWT auth, not what you want to use in production. But for the sake of this project I went with it.

##### DB  
I used Postgres and SQLModel as the ORM. Normally I would use SQLAlchemy, but decided why not try this one — especially since it’s from the creator of FastAPI himself.

And used Alembic for DB migrations.
