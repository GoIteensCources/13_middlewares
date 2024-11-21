from fastapi import APIRouter, Depends, HTTPException

route = APIRouter()


@route.post("/")
async def create_registration():
    ...


@route.get("/read/all/")
async def all_items():
    ...
