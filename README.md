# trade-api-fastapi
# Trade API

This is a Trade API implemented using FastAPI framework. It provides endpoints to manage trades and traders.

## Getting Started

These instructions will guide you on how to set up and run the Trade API on your local machine.

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (version 3.7 or higher)
- Pip (Python package manager)

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
2. Change into the project directory:
cd trade-api

3. Create a virtual environment (optional but recommended):
python -m venv venv

4. Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate

5. Install the required dependencies:
pip install -r requirements.txt

6. Configuration
The Trade API can be configured using environment variables. Create a .env file in the project directory and provide the necessary configuration values. You can use the .env.example file as a template.

7. Running the API
#Start the API server:
uvicorn main:app --reload

The API will be accessible at http://localhost:8000.
