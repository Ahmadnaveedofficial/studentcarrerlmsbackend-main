from dotenv import load_dotenv
import uvicorn

# Load .env BEFORE FastAPI starts
load_dotenv()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
