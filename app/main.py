# from fastapi import FastAPI, Depends
# from .dependencies import get_query_token
from fastapi import FastAPI
from app.routes import items, users, sample_crud
from app.repositories.repository import MySqlRepository


# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


app.include_router(sample_crud.router)
app.include_router(users.router)
app.include_router(items.router)



@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.post("/test-post/")
async def test_post(request_body: dict):
    return request_body