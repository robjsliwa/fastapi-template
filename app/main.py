# from fastapi import FastAPI, Depends
# from .dependencies import get_query_token
from fastapi import FastAPI
from .routes import items, users


# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()


app.include_router(users.router)
app.include_router(items.router)


@app.get("/healthz")
async def healthz():
    return {"status": "ok"}
