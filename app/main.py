from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.utility.pass_gen_and_test import PasswordGenerator, PasswordTest
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

## allow origins for CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://khester-mesa-gamma.vercel.app"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PasswordRequest(BaseModel):
    length: int


class PasswordTestRequest(BaseModel):
    password: str


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/generate_password")
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


@app.post("/test_password")
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
