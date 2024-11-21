from fastapi import APIRouter, Depends, HTTPException


route = APIRouter()


@route.post("/")
async def create_user():
    ...


@route.get("/read/all/")
async def all_users():
    return {"User": "Anonimus"}
