from fastapi import APIRouter, Request, HTTPException
from app.utility.pass_gen_and_test import PasswordGenerator, PasswordTest
from pydantic import BaseModel

router = APIRouter()


class PasswordRequest(BaseModel):
    length: int


class PasswordTestRequest(BaseModel):
    password: str


@router.post("/generate_password")
async def generate_password(request: Request) -> dict:
    body = await request.json()
    if "length" not in body:
        raise HTTPException(status_code=400, detail="Missing 'length' key in request body")

    length = body["length"]
    if length <= 0:
        raise HTTPException(status_code=400, detail="Password length must be greater than 0")

    try:
        pass_gen = PasswordGenerator(length)
        password = pass_gen.get_pass()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    response: dict = {"password": password}
    return response


@router.post("/test_password")
async def test_password(request: Request) -> dict:
    body = await request.json()
    if "password" not in body:
        raise HTTPException(status_code=400, detail="Missing 'password' key in request body")

    password = body["password"]
    if not password:
        raise HTTPException(status_code=400, detail="Password cannot be empty")

    try:
        pass_test = PasswordTest(password)
        entropy, strength = pass_test.test_password()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    response: dict = {"entropy": entropy, "strength": strength}
    return response
