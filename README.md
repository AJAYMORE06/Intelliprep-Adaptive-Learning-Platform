# IntelliPrep – AI-Powered Adaptive Learning Platform

An intelligent learning system designed to personalise technical interview preparation through adaptive questioning, AI-powered answer evaluation, targeted feedback and learning progress tracking.

## 1. Project Overview

IntelliPrep is an AI-powered technical interview preparation platform developed as part of an MSc Data Science and Artificial Intelligence dissertation.

Traditional interview preparation platforms often rely on static question banks and predefined learning paths. IntelliPrep aims to address this limitation through an adaptive learning approach that evaluates a learner's responses, identifies knowledge gaps and provides personalised guidance.

The system follows an adaptive learning workflow:

1. Technical interview question generation
2. Learner submits an answer
3. AI-powered answer evaluation
4. Knowledge gap identification
5. Contextual feedback and learning hints
6. Adaptive question progression
7. Learning progress tracking
8. Learning outcome evaluation

**Research focus:** Investigating whether AI-generated adaptive feedback and personalised learning pathways can improve technical interview preparedness compared with static preparation resources.

## 2. Key Features

### Student Platform

- User registration and authentication.
- Personalised technical interview preparation.
- AI-generated technical questions.
- Questions organised by difficulty.
- Answer submission and AI-powered evaluation.
- Feedback highlighting strengths and areas for improvement.
- Contextual learning hints.
- Learning session tracking.
- Performance scores and progress reports.
- Post-session feedback and usability evaluation.

### Adaptive Learning

IntelliPrep aims to adapt the learning experience based on the learner's performance.

The intended learning workflow incorporates:

- Assessment of submitted answers.
- Identification of areas requiring improvement.
- Targeted hints rather than immediately providing complete answers.
- Progressive question difficulty.
- Tracking of performance across learning sessions.

### Administrator Dashboard

The administrator dashboard provides an overview of platform activity and student performance.

Features include:

- Platform overview and usage metrics.
- Student directory.
- Student learning session history.
- Individual session reports.
- Student feedback and usability insights.
- Technical-stack performance analysis.
- Comparison of lowest and latest completed assessment scores.

Administrator access is protected through backend authentication and authorisation.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, TypeScript |
| Frontend build tool | Vite |
| Backend | Python, FastAPI |
| Database | Supabase PostgreSQL |
| ORM | SQLAlchemy |
| Database migrations | Alembic |
| AI integration | Google Gemini |
| Authentication | JWT-based authentication |
| Frontend hosting | Vercel |
| Backend hosting | Render |
| Version control | Git and GitHub |

## 4. System Architecture

IntelliPrep uses a separate frontend and backend architecture.

```text
                    USER
                      |
                      v
             React + TypeScript
                 (Vercel)
                      |
                HTTPS Requests
                      |
                      v
              FastAPI Backend
                  (Render)
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      Supabase     Gemini      Application
     PostgreSQL      AI          Logic
          |           |           |
          +-----------+-----------+
                      |
                      v
             Evaluation Results
                      |
                      v
              React Frontend
```

### Frontend

The React application provides the student and administrator interfaces. It communicates with the backend through HTTP API requests.

### Backend

The FastAPI application handles:

- Authentication and authorisation.
- User management.
- Learning session management.
- Question generation and evaluation.
- Feedback processing.
- Performance calculations.
- Administrator operations.

### Database

Supabase PostgreSQL stores application data, including user accounts, generated questions, learning attempts, password reset tokens and user feedback.

SQLAlchemy is used for database operations, while Alembic manages database schema migrations.

### AI Integration

Google Gemini is integrated into the learning workflow for AI-powered question generation and answer evaluation.

## 5. Repository Structure

The repository separates the frontend and backend applications.

```text
Intelliprep-Adaptive-Learning-Platform/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.ts
│
├── backend/
│   ├── app/
│   │   ├── dependencies/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── database.py
│   │   └── main.py
│   ├── alembic/
│   ├── alembic.ini
│   └── requirements.txt
│
└── README.md
```

*Note: This is a high-level representation. Additional project files and directories may exist.*

## 6. Live Deployment

The application is deployed using separate hosting services for the frontend and backend.

| Service | Platform | Purpose |
|---|---|---|
| Frontend | Vercel | Hosts the React application |
| Backend | Render | Hosts the FastAPI application |
| Database | Supabase | Managed PostgreSQL database |
| AI | Google Gemini | AI-powered learning functionality |

### Production Configuration

The frontend communicates with the deployed backend using the `VITE_API_BASE_URL` environment variable.

The backend uses its configured frontend origin for Cross-Origin Resource Sharing (CORS).

The deployed services operate independently of the developer's local machine.

**Deployment considerations:**

- Render's free instance may enter a sleep state after inactivity, resulting in a slower initial request.
- Vercel serves the frontend application.
- Supabase provides the persistent database.
- Production credentials must be configured through environment variables, not committed to GitHub.

## 7. Local Development Setup

### Prerequisites

Install the following:

- Node.js and npm.
- Python.
- Git.
- Access to a configured Supabase PostgreSQL database.
- A Google Gemini API key.

### Step 1: Clone the Repository

```bash
git clone https://github.com/AJAYMORE06/Intelliprep-Adaptive-Learning-Platform.git

cd Intelliprep-Adaptive-Learning-Platform
```

### Step 2: Configure the Backend

Navigate to the backend directory:

```bash
cd backend
```

Create and activate a Python virtual environment.

**macOS / Linux:**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv

.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the backend directory.

Add the environment variables required by the backend application.

Example structure:

```env
DATABASE_URL=your_database_connection_string
GEMINI_API_KEY=your_gemini_api_key
FRONTEND_URL=your_frontend_origin
```

The names above must be checked against the actual backend configuration before use. Add any additional variables required by the application.

### Step 3: Configure the Database

Ensure that your Supabase PostgreSQL database is accessible.

Apply the database migrations using Alembic:

```bash
alembic upgrade head
```

For an existing database whose schema is already in place and whose migration history has been verified, the migration baseline may already be stamped at the current revision.

Do not blindly run database creation or stamping commands against an existing production database.

### Step 4: Start the Backend

From the backend directory:

```bash
uvicorn app.main:app --reload
```

The backend will normally be available at:

```text
http://localhost:8000
```

FastAPI interactive API documentation:

```text
http://localhost:8000/docs
```

Health endpoint:

```text
http://localhost:8000/api/health
```

### Step 5: Configure the Frontend

Open a separate terminal and navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Create a `.env` file in the frontend directory:

```env
VITE_API_BASE_URL=http://localhost:8000
```

This points the frontend to the locally running FastAPI backend.

### Step 6: Start the Frontend

```bash
npm run dev
```

Vite normally serves the application at:

```text
http://localhost:5173
```

The frontend and backend must both be running for the complete local application to function.

## 8. Environment Variables and Security

Environment variables are used to configure the application without hardcoding credentials.

| Variable | Application | Purpose |
|---|---|---|
| `VITE_API_BASE_URL` | Frontend | Backend API base URL |
| `DATABASE_URL` | Backend | PostgreSQL connection string |
| `GEMINI_API_KEY` | Backend | Gemini API authentication |
| `FRONTEND_URL` | Backend | Frontend origin configuration |

*Verify the backend variable names against the actual source code and configuration before deployment.*

### Security Guidelines

- Never commit `.env` files.
- Never expose database credentials in frontend code.
- Never expose the Gemini API key to the browser.
- Keep JWT signing secrets private.
- Configure CORS for trusted frontend origins.
- Protect administrator endpoints through backend authorisation.
- Use environment variables for production credentials.
- Rotate credentials immediately if they are accidentally exposed.

## 9. Database Management

Supabase PostgreSQL is used as the application's relational database.

The application currently includes the following database entities:

| Table | Purpose |
|---|---|
| `users` | User accounts and administrator status |
| `generated_questions` | Generated interview questions and session information |
| `learning_attempts` | Submitted answers, evaluation scores and feedback |
| `password_reset_tokens` | Password reset functionality |
| `user_feedback` | Student feedback and usability responses |

Database schema changes are managed through Alembic migrations.

## 10. API Documentation

The backend is built using FastAPI.

When running locally, interactive API documentation is available at:

```text
http://localhost:8000/docs
```

The deployed API documentation is available at:

```text
https://intelliprep-adaptive-learning-platform.onrender.com/docs
```

The health endpoint can be used to check backend availability:

```text
GET /api/health
```

API routes are organised into backend routers. Refer to the FastAPI documentation for the complete list of available endpoints and their request and response schemas.

## 11. Testing and Validation

The application should be validated across the following areas before a release:

- User registration and login.
- Authentication and token refresh.
- Student and administrator access control.
- Question generation.
- Answer submission and evaluation.
- Adaptive question progression.
- Learning hints and feedback.
- Session persistence.
- Student progress reports.
- Feedback submission.
- Administrator dashboard metrics.
- Student session history.
- Production frontend-to-backend communication.
- Database persistence.

Run the frontend production build using:

```bash
npm run build
```

Run any configured backend tests using the project's test configuration.
