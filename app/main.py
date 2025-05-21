from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router

# FastAPI object with attributes
app = FastAPI(
    title="House Price Prediction API",
    version="1.0.0",
    description="APIs",
)

# Serving request from any source
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check container health
@app.get("/health")
async def health():
    return {"status":"success","message": "System up"}

# code modularization
# act as registery and route request to respective endpoint/logic
app.include_router(
    router,
    prefix=f""
)
