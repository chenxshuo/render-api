# FastAPI Service

This is a FastAPI service template ready for deployment on Render.

## Local Development

1. Install dependencies:
```bash
uv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at http://localhost:8000

## API Documentation

Once the server is running, you can access:
- API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /text` - Submit a new text message
  ```json
  {
    "text": "Your message here"
  }
  ```
- `GET /texts` - Get all stored messages (newest first)
  - Optional query parameters:
    - `skip`: Number of records to skip (default: 0)
    - `limit`: Maximum number of records to return (default: 10)

## Deployment on Render

1. Create a PostgreSQL database on Render:
   - Go to your Render dashboard
   - Click "New +" and select "PostgreSQL"
   - Choose a name for your database
   - Select the free plan
   - Click "Create Database"
   - Save the "Internal Database URL" for the next step

2. Create a new Web Service on Render:
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   - Use the following settings:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Add the environment variable:
     - Key: `DATABASE_URL`
     - Value: [Your Internal Database URL from step 1]

3. Deploy your service:
   - The service will automatically deploy when you push changes to your repository
   - Your data will now persist in the PostgreSQL database

## Testing the API

Use the provided `test_api.py` script to test your API:

1. For local testing:
```bash
python test_api.py
```

2. For testing the deployed version:
- Edit `BASE_URL` in `test_api.py` to your Render service URL
- Run the test script
