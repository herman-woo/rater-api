from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from db import create_db_and_tables
from domains.rater.routes import router as rating_router
from domains.exposure.routes import router as expo_router
from domains.credit.routes import router as credit_router
from reference.routes import router as code_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("\n\n           🚀 Starting up Base FastAPI...")
    print("               -By Herman Woo\n\n")

    # Initialize DB tables
    create_db_and_tables()

    yield
    print("\n\n           🛑 Shutting down...\n\n")

app = FastAPI(lifespan=lifespan)

# Basic root endpoint
@app.get("/")
async def root():
    return {"message": "Rater-API is Online!"} 

# Register API routes
app.include_router(rating_router, prefix="/rater")
app.include_router(expo_router)
app.include_router(credit_router)
app.include_router(code_router, prefix="/reference")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)