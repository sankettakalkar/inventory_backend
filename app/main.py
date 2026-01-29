from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes import inventory, reports, external

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inventory Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://inventory-frontend.vercel.app",
        "https://inventory-frontend-gurvz847r-sankettakalkars-projects.vercel.app",
        "https://inventory-frontend-ce8rlqtiu-sankettakalkars-projects.vercel.app",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(inventory.router)
app.include_router(reports.router)
app.include_router(external.router)

@app.get("/health")
def root():
    return {"message": "Inventory API running"}