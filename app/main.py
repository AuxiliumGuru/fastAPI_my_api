from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from app.utility.pass_gen_and_test import PasswordGenerator, PasswordTest
from fastapi.middleware.cors import CORSMiddleware
from app.routers import password_gen_test

app = FastAPI()

# Include routers

app.include_router(password_gen_test.router)

# allow origins for CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://khester-mesa-gamma.vercel.app"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {"Hello": "World"}
