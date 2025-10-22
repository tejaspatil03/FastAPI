from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import students, staff, marks, fee

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins like ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(students.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Server Running"}