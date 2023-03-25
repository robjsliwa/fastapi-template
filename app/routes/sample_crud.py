from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_token_header
from app.repositories.repository import MySqlRepository

router = APIRouter()


@router.get("/sample-crud/{string_id}",tags=["sample-crud"])
async def read_string(string_id: int):
    """
    Retrieve a string with the given ID.
    """
    instance = MySqlRepository()
    instance.get(id=string_id)
    return {"string_id": string_id}


@router.post("/sample-crud/",tags=["sample-crud"])
async def create_string(string: str):
    """
    Create a new string.
    """
    instance = MySqlRepository()
    data = {
        "string_text": string,
        "description": string
    }
    instance.create(data=data)
    return {"string": string}


@router.put("/sample-crud/{string_id}", tags=["sample-crud"])
async def update_string(string_id: int, string: str):
    """
    Update a string with the given ID.
    """
    instance = MySqlRepository()
    data = {
        "string_text": string,
        "description": string
    }
    instance.update(id=string_id, data=data)
    return {"string_id": string_id, "string": string}


@router.delete("/sample-crud/{string_id}",tags=["sample-crud"])
async def delete_string(string_id: int):
    """
    Delete a string with the given ID.
    """
    instance = MySqlRepository()
    instance.delete(id=string_id)
    return {"string_id": string_id}
