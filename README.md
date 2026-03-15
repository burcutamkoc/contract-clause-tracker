=======
# Contract Clause Tracker

A web application for managing and labeling legal contract clauses. Users can upload contract files, automatically parse them into sentences, and label each sentence with predefined clause types.

## Features

- **Contract Upload** — Upload contract files in `.txt` and `.md` formats
- **Automatic Sentence Parsing** — Uploaded contracts are automatically split into individual sentences
- **Sentence Labeling** — Assign clause types to each sentence (e.g., "Limitation of Liability", "Termination for Convenience", "Non-Compete")
- **Progress Tracking** — Track labeling status per contract (not_started, in_progress, completed)
- **Search & Filter** — Filter contracts by name and completion status
- **Dashboard** — Overview of all contracts with progress bars

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python, FastAPI 0.135, SQLAlchemy 2.0, Uvicorn |
| **Frontend** | Angular 21, PrimeNG 21, PrimeFlex, SCSS |
| **Database** | PostgreSQL 15 |
| **Infrastructure** | Docker, Docker Compose |
| **API Documentation** | OpenAPI / Swagger (auto-generated) |

## Architecture

The project follows a layered architecture:

```
Backend (FastAPI)
├── API Controllers     → HTTP endpoint definitions
├── Services            → Business logic layer
├── Repositories        → Data access layer
├── Entities            → SQLAlchemy database models
└── Config              → Application settings & seed data

Frontend (Angular)
├── Pages               → Dashboard, Upload, Labeler pages
├── Components          → ContractTable, SentenceLabeler components
└── API Services        → Auto-generated via OpenAPI Generator
```

## Design Decisions

### Simple Backend Structure
The backend follows a simple layered structure (Controller → Service → Repository).
This keeps the business logic separate from the HTTP layer while still keeping the implementation minimal, as the goal of this case study was to focus on a clean but lightweight backend.

### Sentence-Based Clause Modeling
Contracts are parsed into individual sentences, and each sentence can be labeled with a clause type.  
This matches the assumption of the assignment that a legal clause corresponds to a single sentence.

### Angular Feature-Based Frontend Structure
The frontend uses a feature-based folder structure.  
Each feature (e.g., contracts) contains its own pages, components, and logic, which improves maintainability and scalability.

### PrimeNG UI Components
PrimeNG was used to build the UI quickly while maintaining a consistent and clean design.  
Components such as tables, cards, progress bars, and toolbars helped create an intuitive dashboard and labeling interface.

### Dockerized Environment
Docker and Docker Compose are used so the entire application (frontend, backend, database) can be started with a single command.

## Database Schema

```
contracts              sentences              clause_types
┌──────────────┐      ┌──────────────────┐   ┌──────────────┐
│ id (PK)      │      │ id (PK)          │   │ id (PK)      │
│ name         │──1:N─│ contract_id (FK)  │   │ name         │
│ content      │      │ text             │   └──────┬───────┘
│ created_at   │      │ order            │          │
└──────────────┘      └──────┬───────────┘          │
                             │                      │
                      sentence_labels               │
                      ┌──────────────────┐          │
                      │ id (PK)          │          │
                      │ sentence_id (FK) │──────────┘
                      │ clause_type_id(FK)│
                      └──────────────────┘
```

## API Endpoints

### Contracts (`/contracts`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/contracts` | List all contracts (with status and search filters) |
| `GET` | `/contracts/{id}` | Get contract details |
| `POST` | `/contracts` | Create contract from JSON |
| `POST` | `/contracts/upload` | Upload contract from file |
| `DELETE` | `/contracts/{id}` | Delete a contract |

### Sentences (`/sentences`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/contracts/{id}/sentences` | List sentences for a contract with their labels |
| `POST` | `/sentences/{id}/label` | Assign a label to a sentence |

### Clause Types (`/clause-types`)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/clause-types` | List all clause types |
| `POST` | `/clause-types` | Create a new clause type |

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose

### Quick Start

```bash
# Clone the repository
git clone <repo-url>
cd contract_clause_tracker

# Start all services with Docker Compose
docker-compose up
```

Once the application is running:

| Service | URL |
|---------|-----|
| **Frontend** | http://localhost:4200 |
| **Backend API** | http://localhost:8000 |
| **Swagger Docs** | http://localhost:8000/docs |

### Running Services Individually

#### Backend

```bash
cd backend
pip install -r requirements.txt
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/contracts
uvicorn main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npx ng serve --host 0.0.0.0
```

## Usage Workflow

1. **Dashboard** — View all existing contracts on the main page
2. **Upload** — Click "Upload Contract" to upload a new contract file
3. **Label** — The contract is automatically split into sentences; select the appropriate clause type for each sentence
4. **Track** — Monitor labeling progress via the progress bar on the dashboard

## Project Structure

```
contract_clause_tracker/
├── docker-compose.yml
├── backend/
│   ├── main.py                          # FastAPI application entry point
│   ├── requirements.txt                 # Python dependencies
│   ├── local.env                        # Environment variables
│   └── src/
│       ├── api/controller/              # API endpoints
│       ├── core/
│       │   ├── models/                  # Pydantic request/response models
│       │   └── service/                 # Business logic services
│       └── infra/
│           ├── config/                  # App configuration & seed data
│           └── repository/
│               ├── entities/            # SQLAlchemy entity models
│               └── *_repository.py      # Data access layer
├── frontend/
│   └── src/app/
│       ├── core/api/                    # Auto-generated API services
│       └── features/contracts/
│           ├── components/              # Reusable UI components
│           └── pages/                   # Page components
└── examples/
    └── sample_contract.txt              # Sample contract file
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://postgres:postgres@db:5432/contracts` |

## Testing

API endpoints were manually tested using Swagger and Postman during development to verify the main flows:

- Contract upload
- Sentence parsing
- Clause labeling
- Dashboard listing

## License

This project was developed for Legartis.
>>>>>>> f1a32c4 (feat: contract clause tracker)
