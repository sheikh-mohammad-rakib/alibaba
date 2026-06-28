# Qwen Agent PoC

This is a Proof of Concept (PoC) FastAPI application that integrates with Alibaba Cloud's Qwen large language models via DashScope. It demonstrates how to create a simple chat API using the OpenAI Python client library configured to use DashScope's compatible mode.

## Features

- **FastAPI**: High-performance asynchronous web framework.
- **OpenAI Client Integration**: Uses the standard OpenAI Python client to interact with DashScope, making it easy to swap models or providers.
- **Qwen Model**: Uses the `qwen3.7-plus` model for chat completions.
- **Environment Configuration**: Uses `python-dotenv` and `pydantic-settings` for secure management of API keys.

## Prerequisites

- Python 3.9+
- A valid DashScope API Key from Alibaba Cloud.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sheikh-mohammad-rakib/alibaba.git
   cd alibaba
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root of the project and add your DashScope API key:

```env
DASHSCOPE_API_KEY=your_dashscope_api_key_here
```

## Running the Application

Start the FastAPI development server using Uvicorn:

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns the status of the service.

### 2. Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Simple health check endpoint.

### 3. Chat Endpoint
- **URL**: `/chat`
- **Method**: `POST`
- **Description**: Send a list of messages to the Qwen model and receive a completion.
- **Request Body**:
  ```json
  {
    "messages": [
      {
        "role": "user",
        "content": "Hello! What can you do?"
      }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "response": "Hello! I am a large language model created by Alibaba Cloud..."
  }
  ```

## API Documentation

Once the server is running, you can view the interactive Swagger UI documentation at:
- `http://localhost:8000/docs`
