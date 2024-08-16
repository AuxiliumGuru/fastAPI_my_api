from fastapi import APIRouter, Request, HTTPException
from app.utility.random_facts import random_fact
from pydantic import BaseModel

router = APIRouter()

fact = random_fact.Fact()


@router.get("/facts/random")
def get_random_fact() -> dict:
    return {"fact": fact.get_random_fact()}


@router.get("/facts/today")
def get_today_random_fact() -> dict:
    return {"fact": fact.get_today_random_fact()}
