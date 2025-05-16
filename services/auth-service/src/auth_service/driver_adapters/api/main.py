import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="Authentication Service",
    description="Microservice for user authentication and authorization",
    version="0.1.0",
)


@app.get("/", tags=["Health"])
async def health_check():
    """check my service health"""
    return {"status": "ok", "service": "auth-service"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
