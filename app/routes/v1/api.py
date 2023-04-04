from fastapi import APIRouter
from .endpoints import sample_crud

api_router = APIRouter(responses={404: {"description": "Not found"}})
api_router.include_router(sample_crud.router, prefix='/v1',
						  tags=['sample-crud'])
