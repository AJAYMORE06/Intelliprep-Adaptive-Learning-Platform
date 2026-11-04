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
- Voice-based answer recording and transcription.
- Learning session tracking.
- Performance scores and progress reports.
- Post-session feedback and usability evaluation.

### Adaptive Learning

IntelliPrep adapts the learning experience based on the learner's performance.

The learning workflow incorporates:

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
| Speech recognition | faster-whisper |
| Audio processing | FFmpeg, PyAV |
| Authentication | JWT-based authentication |
| Frontend hosting | Vercel |
| Backend hosting | Oracle Cloud Infrastructure |
| Web server / Reverse proxy | Nginx |
| Backend process management | systemd |
| HTTPS | Let's Encrypt / Certbot |
| Version control | Git and GitHub |

## 4. System Architecture

IntelliPrep uses a separate frontend and backend architecture.

The React frontend is hosted on Vercel, while the FastAPI backend runs on an Oracle Cloud virtual machine. Vercel rewrites API requests to the Oracle-hosted backend, maintaining a consistent frontend origin for API communication and authentication cookies.

```text
                       USER
                         |
                         v
                React + TypeScript
                     (Vercel)
                         |
                         v
                 HTTPS API Requests
                         |
                         v
                  Vercel API Rewrite
                         |
                         v
                  Oracle Cloud VM
                         |
                         v
                       Nginx
                         |
                         v
                  FastAPI Backend
                    (Uvicorn)
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
      Supabase        Google         faster-whisper
     PostgreSQL       Gemini          (Local CPU)
          |              |              |
          +--------------+--------------+
                         |
                         v
                 Evaluation Results
                         |
                         v
                  React Frontend
```

### Frontend

The React application provides student and administrator interfaces. It communicates with the backend through HTTP API requests.

Vercel hosts the production frontend and forwards `/api/*` requests to the Oracle backend through configured rewrites.

### Backend

The FastAPI application handles:

- Authentication and authorisation.
- User management.
- Learning session management.
- Question generation and evaluation.
- Feedback processing.
- Performance calculations.
- Speech transcription.
- Administrator operations.

Uvicorn runs the application locally on the Oracle VM, while Nginx handles incoming HTTPS requests and forwards them to the FastAPI service.

### Database

Supabase PostgreSQL stores application data, including user accounts, generated questions, learning attempts, password reset tokens and user feedback.

SQLAlchemy is used for database operations, while Alembic manages database schema migrations.

The database remains externally hosted and is accessed securely by the Oracle backend.

### AI Integration

Google Gemini is integrated into the learning workflow for AI-powered question generation and answer evaluation.

### Speech Recognition

The application uses `faster-whisper` for locally hosted speech recognition.

The Whisper model runs on the Oracle VM using CPU inference with the `base.en` model and `int8` computation.

Audio is processed by the backend rather than requiring a separate hosted transcription service.

## 5. Repository Structure

The repository separates the frontend and backend applications.

```text
Intelliprep-Adaptive-Learning-Platform/
|
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── types/
│   ├── package.json
│   ├── package-lock.json
│   ├── vercel.json
│   └── vite.config.ts
|
├── backend/
│   ├── app/
│   │   ├── dependencies/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── database.py
│   │   └── main.py
│   ├── alembic/
│   ├── alembic.ini
│   └── requirements.txt
|
└── README.md
```

*Note: This is a high-level representation. Additional project files and directories may exist.*

## 6. Live Deployment

The production application uses separate hosting services for its frontend and backend.

| Service | Platform | Purpose |
|---|---|---|
| Frontend | Vercel | Hosts the React application |
| Backend | Oracle Cloud Infrastructure | Hosts the FastAPI application |
| Reverse proxy | Nginx | Handles HTTPS and forwards API requests |
| Database | Supabase | Managed PostgreSQL database |
| AI | Google Gemini | Question generation and answer evaluation |
| Speech recognition | faster-whisper | Local audio transcription |
| SSL certificate | Let's Encrypt | HTTPS certificate |

### Production Frontend

The production frontend is deployed on Vercel.

Production URL:

https://intelliprep-adaptive-learning-platf-alpha.vercel.app

The frontend uses the `VITE_API_BASE_URL` environment variable to determine its API base URL.

Production configuration:

```env
VITE_API_BASE_URL=https://intelliprep-adaptive-learning-platf-alpha.vercel.app
```

### Vercel API Rewrites

The frontend contains a `vercel.json` configuration that forwards API requests to the Oracle backend.

Example:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "https://132.145.51.234/api/:path*"
    },
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

The API rewrite must appear before the frontend SPA fallback.

This configuration allows browser requests to use the Vercel domain while the actual API processing takes place on Oracle Cloud.

### Oracle Cloud Backend

The FastAPI backend is hosted on an Oracle Cloud Infrastructure virtual machine.

Deployment environment:

| Property | Configuration |
|---|---|
| Cloud provider | Oracle Cloud Infrastructure |
| Region | London |
| Operating system | Ubuntu 24.04 LTS |
| Architecture | ARM64 |
| Instance shape | VM.Standard.A1.Flex |
| CPU allocation | 2 OCPUs |
| Memory allocation | 12 GB |
| Backend framework | FastAPI |
| Application server | Uvicorn |
| Reverse proxy | Nginx |

Production API base URL:

https://132.145.51.234

FastAPI documentation:

https://132.145.51.234/docs

Health endpoint:

https://132.145.51.234/api/health

### Backend Process Management

The FastAPI application runs as a systemd service named:

```text
intelliprep.service
```

The service manages the backend process and is configured to start automatically when the VM boots.

Useful service commands:

```bash
sudo systemctl status intelliprep
sudo systemctl restart intelliprep
sudo systemctl stop intelliprep
sudo systemctl start intelliprep
```

View application logs:

```bash
sudo journalctl -u intelliprep -f
```

### Nginx and HTTPS

Nginx acts as a reverse proxy between incoming HTTPS requests and the local FastAPI application.

The FastAPI application listens on:

```text
127.0.0.1:8000
```

Nginx forwards requests to this local address.

HTTPS is configured using a Let's Encrypt IP-address certificate managed through Certbot.

Useful commands:

```bash
sudo systemctl status nginx
sudo nginx -t
sudo systemctl reload nginx
sudo certbot certificates
```

Certificate renewal should be verified periodically.

### Production Configuration

Production credentials and application settings are stored in environment variables rather than committed to GitHub.

The frontend and backend operate independently of the developer's local machine.

## 7. Local Development Setup

### Prerequisites

Install the following:

- Node.js and npm.
- Python.
- Git.
- Access to a configured Supabase PostgreSQL database.
- A Google Gemini API key.
- FFmpeg for audio-processing functionality.

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

Install FFmpeg if it is not already available on your system.

Create a `.env` file in the backend directory.

Example configuration:

```env
DATABASE_URL=your_database_connection_string

JWT_SECRET_KEY=your_jwt_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=your_access_token_expiry
REFRESH_TOKEN_EXPIRE_DAYS=your_refresh_token_expiry

GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_gemini_model

RESEND_API_KEY=your_resend_api_key
EMAIL_FROM=your_verified_sender_address

ENVIRONMENT=development
FRONTEND_URL=http://localhost:5173
```

Use the actual variable names and values required by the backend source code. Never commit the `.env` file.

### Step 3: Configure the Database

Ensure that your Supabase PostgreSQL database is accessible.

Apply database migrations when required:

```bash
alembic upgrade head
```

For an existing database whose schema and migration history are already in place, do not blindly run database creation, migration or stamping commands.

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

Create a `.env.local` file in the frontend directory:

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
| `JWT_SECRET_KEY` | Backend | JWT signing secret |
| `JWT_ALGORITHM` | Backend | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Backend | Access-token lifetime |
| `REFRESH_TOKEN_EXPIRE_DAYS` | Backend | Refresh-token lifetime |
| `GEMINI_API_KEY` | Backend | Gemini API authentication |
| `GEMINI_MODEL` | Backend | Gemini model configuration |
| `RESEND_API_KEY` | Backend | Email service authentication |
| `EMAIL_FROM` | Backend | Configured email sender |
| `ENVIRONMENT` | Backend | Application environment |
| `FRONTEND_URL` | Backend | Frontend origin configuration |

### Security Guidelines

- Never commit `.env` files.
- Never expose database credentials in frontend code.
- Never expose the Gemini API key to the browser.
- Keep JWT signing secrets private.
- Configure CORS for trusted frontend origins.
- Protect administrator endpoints through backend authorisation.
- Use environment variables for production credentials.
- Use HTTPS for production API communication.
- Keep authentication cookies secure and HTTP-only.
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

The Oracle-hosted backend connects to the existing Supabase PostgreSQL database. The application does not require a separate database hosted on the Oracle VM.

## 10. API Documentation

The backend is built using FastAPI.

When running locally, interactive API documentation is available at:

```text
http://localhost:8000/docs
```

The production API documentation is available at:

```text
https://132.145.51.234/docs
```

The health endpoint can be used to check backend availability:

```text
GET /api/health
```

API routes are organised into backend routers. Refer to the FastAPI documentation for the complete list of available endpoints and their request and response schemas.

## 11. Testing and Validation

The application should be validated across the following areas before a release:

### Authentication

- User registration and login.
- Refresh-token authentication.
- Logout and session termination.
- Student and administrator access control.
- Password reset and email delivery.

### Learning Workflow

- Question generation.
- Answer submission and evaluation.
- Adaptive question progression.
- Learning hints and feedback.
- Voice recording and transcription.
- Session persistence.
- Student progress reports.

### Administration

- Administrator dashboard metrics.
- Student session history.
- Individual session reports.
- Student feedback.
- Technical-stack performance analysis.

### Infrastructure

- Production frontend-to-backend communication.
- Database connectivity and persistence.
- HTTPS certificate validity.
- Backend service availability.
- Nginx reverse proxy functionality.

Run the frontend production build using:

```bash
cd frontend
npm run build
```

Run configured backend tests using the project's test configuration.

## 12. Production Deployment and Maintenance

The production environment consists of a Vercel frontend and an Oracle Cloud-hosted FastAPI backend.

### Frontend Deployment

Frontend changes are deployed through Vercel.

Before deployment:

```bash
cd frontend
npm run build
```

Verify that the production environment variables are configured correctly.

### Backend Deployment

Backend changes are deployed to the Oracle Cloud virtual machine.

The deployment process includes:

1. Updating the backend source code.
2. Installing or updating dependencies when necessary.
3. Verifying environment configuration.
4. Testing application imports and configuration.
5. Restarting the `intelliprep` systemd service.
6. Checking the application health endpoint.
7. Reviewing backend logs.

### Useful Operational Commands

Check backend status:

```bash
sudo systemctl status intelliprep
```

Restart the backend:

```bash
sudo systemctl restart intelliprep
```

Follow backend logs:

```bash
sudo journalctl -u intelliprep -f
```

Check Nginx status:

```bash
sudo systemctl status nginx
```

Test Nginx configuration:

```bash
sudo nginx -t
```

Check disk usage:

```bash
df -h
```

Check memory usage:

```bash
free -h
```

Check HTTPS certificates:

```bash
sudo certbot certificates
```

Production maintenance should include periodic database backups, certificate-renewal checks, application log reviews and Oracle resource monitoring.

---

## 13. Project Objective

IntelliPrep aims to demonstrate how AI-powered evaluation, adaptive questioning, targeted feedback and personalised learning pathways can support technical interview preparation.

The platform combines modern frontend development, cloud-hosted backend infrastructure, relational data management, generative AI and locally hosted speech recognition into an integrated intelligent learning system.
