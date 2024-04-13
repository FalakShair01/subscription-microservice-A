```markdown
# Subscription Microservice

This microservice is responsible for managing subscriptions. It communicates with Service B to synchronize subscription status updates.

## Description

The Subscription Microservice is a component of a larger system responsible for managing subscription status across different services. It provides an API for creating, retrieving, updating, and deleting subscriptions. The microservice ensures consistent subscription status updates by communicating with Service B using RabbitMQ.

## Directory Structure

```
subscription_microservice/
│
├── config/
│   ├── database.py        # Configuration for database connection
│   └── __init__.py
│
├── model/
│   ├── __init__.py
│   └── models.py           # SQLAlchemy models for database tables
│
├── routers/
│   ├── __init__.py
│   └── subscription.py    # FastAPI routers for handling subscription endpoints
│
├── schemas/
│   ├── __init__.py
│   └── schema.py          # Pydantic schemas for request and response data
│
├── dependencies/
│   ├── __init__.py
│   └── subscription_service.py  # Business logic for subscription management
│
├── main.py                 # FastAPI application setup
├── README.md              # Documentation file
└── requirements.txt       # Project dependencies
```

## Workflow

1. **Request Handling**: FastAPI routers in the `routers` directory handle incoming HTTP requests.
2. **Business Logic**: The business logic for subscription management is implemented in the `subscription_service.py` module inside the `dependencies` directory.
3. **Database Interaction**: Database operations are managed by functions in the `database.py` module inside the `config` directory. SQLAlchemy models for database tables are defined in the `model.py` module inside the `models` directory.
4. **Request/Response Data**: Pydantic schemas for request and response data are defined in the `schema.py` module inside the `schemas` directory.

## Setup

1. **Clone the Repository**: `git clone https://github.com/FalakShair01/subscription-microservice-A.git`
2. **Navigate to the Project Directory**: `cd subscription-microservice-A`
3. **Create a Virtual Environment**: `python3 -m venv venv`
4. **Activate the Virtual Environment**:
    - On Windows: `venv\Scripts\activate`
    - On macOS and Linux: `source venv/bin/activate`
5. **Install Requirements**: `pip install -r requirements.txt`

## Usage

1. **Run the FastAPI Server**: `uvicorn app:app --reload`
2. **Access the API**: The API is now running locally at `http://localhost:8000`.

## Dependencies

- Python 3.7+
- FastAPI
- SQLAlchemy
- Pydantic
- uvicorn
- rabbitMQ

## Notes

- Ensure that Service B is running and accessible to synchronize subscription status updates using RabbitMQ.
- Update the database configuration in `config/database.py` as needed.
```
