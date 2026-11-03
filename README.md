IntelliPrep – AI-Powered Personalised Technical Interview Preparation
1. About the Project
IntelliPrep is an AI-powered intelligent learning system designed to help users prepare for technical interviews through personalised practice, adaptive question difficulty and AI-generated feedback.
The application aims to improve interview readiness by identifying knowledge gaps and guiding learners through an adaptive learning experience.
Key Features
* User registration and authentication.
* Personalised technical interview preparation.
* Adaptive question difficulty.
* AI-powered answer evaluation.
* Contextual feedback and hints.
* Learning progress and performance tracking.
* Student dashboard.
* Administrator dashboard and performance monitoring.
2. Technology Stack
Component	Technology
Frontend	React.js
Frontend tooling	Vite
Programming language	TypeScript / JavaScript
Backend	Python
Backend framework	FastAPI
Database	PostgreSQL
ORM	SQLAlchemy
AI integration	Google Gemini API
API communication	REST API
3. Prerequisites
Install the following software before setting up IntelliPrep.
3.1 Node.js and npm
Node.js is required to run the React frontend. npm is included with Node.js.
Download: https://nodejs.org/
Recommended: Install the current LTS version.
Verify installation:
node -v
npm -v
Both commands should display their installed versions.
3.2 Python
Python is required to run the FastAPI backend.
Download: https://www.python.org/downloads/
Recommended: Python 3.11 or the version specified by the project dependencies.
Verify installation:
python3 --version
3.3 PostgreSQL
IntelliPrep uses PostgreSQL as its relational database.
Download PostgreSQL for macOS:
https://www.postgresql.org/download/macosx/
For macOS, beginners can use the graphical installer provided by EDB.
During installation:
* Install the PostgreSQL server.
* Install the command-line tools.
* Set a password for the postgres database user.
* Keep the default port as 5432, unless it is already occupied.
* Remember the password because it will be required when connecting the backend.
Verify installation:
psql --version
3.4 Code Editor
Visual Studio Code is recommended.
Download: https://code.visualstudio.com/
4. Clone the Repository
Open Terminal and navigate to the directory where you want to store the project.
Clone the repository:
git clone YOUR_GITHUB_REPOSITORY_URL
Navigate into the project:
cd IntelliPrep
Replace the repository URL with the actual GitHub repository URL.
5. Project Structure
The expected project structure is:
IntelliPrep/
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── database.py
│   └── ...
│
└── README.md
Note: These are illustrative folder names. Use the actual directory names from the GitHub repository.
6. Database Setup – PostgreSQL
Step 1: Start PostgreSQL
On macOS, if PostgreSQL was installed using Homebrew:
brew services list
Start the appropriate installed PostgreSQL version. For example:
brew services start postgresql@16
If you installed PostgreSQL using the EDB graphical installer, start the PostgreSQL server through its installed application or service controls.
Check whether the server is accepting connections:
pg_isready
Step 2: Connect to PostgreSQL
psql -U postgres -h localhost -p 5432
Enter your PostgreSQL password when prompted.
Step 3: Create the IntelliPrep Database
Inside the PostgreSQL command-line interface, execute:
CREATE DATABASE intelliprep;
List available databases:
\l
Connect to IntelliPrep:
\c intelliprep
Exit PostgreSQL:
\q
Step 4: Database Connection
The backend needs a database connection string.
The general PostgreSQL connection format is:
postgresql://USERNAME:PASSWORD@HOST:PORT/DATABASE_NAME
Example:
postgresql://postgres:your_password@localhost:5432/intelliprep
Use the actual credentials configured during PostgreSQL installation.
7. Backend Setup – FastAPI
Step 1: Navigate to the Backend Directory
cd backend
Replace backend with the actual backend folder name if different.
Step 2: Create a Python Virtual Environment
python3 -m venv venv
Step 3: Activate the Environment
For macOS/Linux:
source venv/bin/activate
For Windows:
venv\Scripts\activate
Step 4: Install Dependencies
If the repository contains requirements.txt:
pip install -r requirements.txt
Otherwise, install the dependencies specified by the project's Python dependency configuration.
Step 5: Configure Environment Variables
Create a .env file in the location expected by the backend configuration.
Example configuration:
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/intelliprep

GEMINI_API_KEY=your_gemini_api_key

SECRET_KEY=your_secure_secret_key
Important:
* Use the environment variable names expected by the actual backend code.
* Obtain a Gemini API key from https://aistudio.google.com/apikey
* Generate a strong secret key.
* Never commit .env to GitHub.
* Keep production credentials separate from local development credentials.
Step 6: Start the Backend
If the FastAPI application entry point is main.py and the application variable is app:
uvicorn main:app --reload
If your application is inside a package or uses a different entry point, adjust the command accordingly.
The backend should become available at:
http://127.0.0.1:8000
Step 7: Access API Documentation
FastAPI provides interactive API documentation.
Open:
http://127.0.0.1:8000/docs
You can use this interface to inspect and test available API endpoints.
8. Frontend Setup – React and Vite
Open a second Terminal window.
Step 1: Navigate to the Frontend Directory
cd IntelliPrep/frontend
Use the actual frontend folder name.
Step 2: Install npm Dependencies
npm install
This installs the dependencies listed in package.json.
Step 3: Configure Frontend Environment Variables
If the frontend uses an environment variable for the backend API URL, create the appropriate .env file.
For example:
VITE_API_BASE_URL=http://127.0.0.1:8000
The variable name must match the one referenced in your React application.
Do not place Gemini API keys, database passwords or backend secrets in frontend environment variables. Vite variables are exposed to the browser.
Step 4: Start the Frontend
npm run dev
The Vite development server will normally run at:
http://localhost:5173
Open the URL in your browser.
9. Running the Complete Application
IntelliPrep requires PostgreSQL, the FastAPI backend and the React frontend to be running.
Start each service in a separate Terminal window.
Terminal 1 – PostgreSQL
Ensure the PostgreSQL server is running.
pg_isready
Terminal 2 – Backend
cd backend
source venv/bin/activate
uvicorn main:app --reload
Terminal 3 – Frontend
cd frontend
npm run dev
Open:
http://localhost:5173
The frontend communicates with the FastAPI backend, which connects to PostgreSQL and uses the configured Gemini API integration.
10. First-Time Usage
Once the application is running:
1. Open the application in your browser.
2. Register or log in using the available authentication functionality.
3. Navigate to the student dashboard.
4. Start a technical interview preparation session.
5. Attempt the questions presented by the system.
6. Review the AI-generated evaluation and feedback.
7. Follow the adaptive question progression.
8. Review your performance and learning progress.
Administrator functionality is available to authorised administrator accounts.
11. Troubleshooting
Problem: npm: command not found
Node.js and npm may not be installed or configured correctly.
Check:
node -v
npm -v
Install Node.js LTS from https://nodejs.org/.
Problem: psql: command not found
PostgreSQL command-line tools may not be installed or available in your PATH.
Check your PostgreSQL installation and command-line tool configuration.
Problem: PostgreSQL is not accepting connections
Check:
pg_isready
On Homebrew installations:
brew services list
Start the correct PostgreSQL service if it is stopped.
Problem: Database connection refused
Check the following:
* PostgreSQL is running.
* The database exists.
* The host and port are correct.
* The database username and password are correct.
* The backend is loading the correct environment variables.
Problem: ModuleNotFoundError
Ensure the backend virtual environment is activated.
Install the dependencies again:
pip install -r requirements.txt
Problem: Frontend cannot communicate with backend
Check:
* FastAPI is running.
* The frontend API URL is correct.
* FastAPI CORS configuration permits the frontend origin.
* The browser console and backend logs for errors.
Problem: Gemini API errors
Check:
* The API key is valid.
* The key is configured in the backend environment.
* API access and usage limits are available.
* The backend is reading the correct environment variable.
12. Security Guidelines
* Never commit .env files.
* Never expose database credentials in frontend code.
* Never expose Gemini API keys in browser-accessible code.
* Use secure authentication and role-based authorisation.
* Protect administrator endpoints on the backend.
* Validate user input on the server.
* Use HTTPS for production deployment.
* Back up the PostgreSQL database regularly.
* Avoid using default or weak passwords.
13. Useful Commands
Task	Command
Check Node.js	node -v
Check npm	npm -v
Check Python	python3 --version
Check PostgreSQL	psql --version
Check PostgreSQL status	pg_isready
Install frontend dependencies	npm install
Run frontend	npm run dev
Create virtual environment	python3 -m venv venv
Activate virtual environment	source venv/bin/activate
Install backend dependencies	pip install -r requirements.txt
Run FastAPI	uvicorn main:app --reload
14. Deployment
The application can be deployed using cloud hosting services.
A possible deployment architecture is:
Component	Hosting
React frontend	Vercel
FastAPI backend	Render
PostgreSQL database	Supabase
Source control	GitHub
Production deployment requires separate environment variables and a production database connection.
For academic research, maintain database backups and avoid resetting the production database after participant data collection begins.

15. Support and Contribution
For development or setup issues, review the repository documentation and application logs.
Contributions, suggestions and improvements are welcome.
IntelliPrep – Personalised Learning for Better Technical Interview Preparation.
