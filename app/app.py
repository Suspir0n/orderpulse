from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
async def health_check():
    return {
        "status_code": 200,
        "data": {
            "status": "OK",
        }
    }