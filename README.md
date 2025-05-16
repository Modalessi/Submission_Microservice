# KP TASK (Submission Microservice)

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
        "user_id": uuid.UUID,
        "problem_id": uuid.UUID,
        "language": str,
        "source_code": str,
        "status": SubmissionStatus,
        "result": SubmissionResult | None,
        "execution_time": int | None
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
DB_URL=postgresql://user:password@postgres:5432/submissions
REDIS_URL=redis
RATE_LIMIT=5
TIME_WINDOW=60
JWT_SECRET=your-secret-key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Running with Docker
```bash
docker-compose up -d
```

### Running for Development
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Future Improvements
- Add comprehensive test suite
- Implement more advanced code evaluation strategies
- Add pagination for submission listings
- Enhance error handling and validation