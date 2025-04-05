# FastAPI Service

This is a FastAPI service template ready for deployment on Render.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
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

## Deployment on Render

1. Push this repository to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Use the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
