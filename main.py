import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from routers import route

app = FastAPI(description="Learning Middlewares",
              version="0.1")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get("/hello")
async def hello_rout(user: str = "Anonimus"):
    return f"Hello, {user}!"


app.include_router(route, prefix="/movies", tags=["movie"])

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
