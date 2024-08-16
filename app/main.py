from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import password_gen_test, todos, facts

app = FastAPI()

# Include routers

app.include_router(password_gen_test.router)
app.include_router(todos.router)
app.include_router(facts.router)
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
    return {
        "Hello": "World",
        "About": {
            "description": "This is a FastAPI project for my hobby projects",
            "author": "Allan Mesa",
            "email": "khestermesa@gmail.com"
        }
    }
