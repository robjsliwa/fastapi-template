from fastapi import FastAPI
from app.repositories.repository import MySqlRepository
from app.routes.v1.api import api_router

app = FastAPI()
app.include_router(api_router)


@app.get("/healthz")
async def healthz():
	return {"status": "ok"}
