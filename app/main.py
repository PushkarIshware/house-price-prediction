from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
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

# Check cotainer health
@app.get("/health")
async def health():
    return {"status":"success","message": "System up"}


@app.get("api/house-price-prediction/docs", include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(
        openapi_url="api/house-price-prediction/docs/openapi.json",
        title="House Price Prediction API",
    )


@app.get("api/house-price-prediction/docs/openapi.json", include_in_schema=False)
async def openapi():
    return get_openapi(title="House Price Prediction API", version=app.version, routes=app.routes)

# code modularization
# act as registery and route request to respective endpoint/logic
app.include_router(
    router,
    prefix=f""
)
