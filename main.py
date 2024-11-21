import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse


app = FastAPI(description="Learning Middlewares",
              version="0.1")


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get("/hello")
async def example_rout():
    time.sleep(0.1)
    print("body of route")
    return "Hello World!"


# app.include_router(route, prefix="/movies", tags=["movie"])

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)
