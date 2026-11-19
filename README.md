# Eldoret Hardware — Credit Balance Lookup

A lightweight Flask web application and JSON API for **Eldoret Hardware** to look up customer credit balances in Kenyan Shillings (`KES`) and view all debtor records.

## Features

- **Web Interface (`/`)**: Simple search form using `fetch` to look up a customer's balance without reloading the page.
- **Balance Lookup API (`GET /api/balance?name=<customer_name>`)**: Case-insensitive customer lookup returning JSON with proper HTTP status codes (`200`, `400`, `404`).
- **All Debtors API (`GET /debtors`)**: Returns the full dictionary of customers and their `KES` balances as JSON.

## Project Structure

```text
.
├── app.py          # Flask application, HTML template, and API routes
└── README.md       # Project documentation
```

## Prerequisites

- Python **3.8+**
- **Flask**

## Setup & Installation

1. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows (Command Prompt):
   venv\Scripts\activate
   # On Windows (PowerShell):
   venv\Scripts\Activate.ps1
   ```

2. **Install Flask**:

   ```bash
   pip install flask
   ```

## Running the Application

Start the development server:

```bash
python app.py
```

Open your browser and go to:

```text
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```

## API Endpoints

### 1. Check Customer Balance
- **Endpoint:** `GET /api/balance`
- **Query Parameter:** `name` (string, required)
- **Example Request:**
  ```text
  GET [http://127.0.0.1:5000/api/balance?name=Brian%20Keyo](http://127.0.0.1:5000/api/balance?name=Brian%20Keyo)
  ```
- **Success Response (`200 OK`):**
  ```json
  {
    "customer": "Brian Keyo",
    "balance": 50000
  }
  ```
- **Error Responses:**
  - `400 Bad Request` — Missing or empty `name` parameter:
    ```json
    {
      "error": "Please provide a customer name."
    }
    ```
  - `404 Not Found` — No matching customer found:
    ```json
    {
      "error": "Customer 'Unknown Name' not found."
    }
    ```

### 2. List All Debtors
- **Endpoint:** `GET /debtors`
- **Example Request:**
  ```text
  GET [http://127.0.0.1:5000/debtors](http://127.0.0.1:5000/debtors)
  ```
- **Response (`200 OK`):**
  ```json
  {
    "Brian Keyo": { "KES": 50000 },
    "Mallory Odongo": { "KES": 21000 },
    "Keith Ken": { "KES": 39192 },
    "Jayden Okoth": { "KES": 48342 },
    "Stephen Mei": { "KES": 10100 }
  }
  ```

## Notes

- Customer data is currently stored in memory (`customer_name` dictionary in `app.py`), so changes will not persist across server restarts.
- `debug=True` is enabled for local development; disable debug mode before deploying to production.

## Pricing
For KES 5,000 per month you can get this lightweight flask.
