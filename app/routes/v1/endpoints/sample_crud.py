from fastapi import APIRouter, Depends, HTTPException, status
from app.dependencies import get_token_header
from app.repositories.repository import MySqlRepository
import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/sample-crud/{string_id}",tags=["sample-crud"])
async def read_string(string_id: int):
    """
    Retrieve a string with the given ID.
    """
    logger.info("Retrieving string: %s", string_id)
    instance = MySqlRepository()
    resp = instance.get(id=string_id)
    return {"string_id": resp}



@router.post("/sample-crud/", tags=["sample-crud"], status_code=status.HTTP_201_CREATED)
async def create_string(data: dict):
    """
    Create a new string.
    """
    logger.info("Creating string: %s", data)
    instance = MySqlRepository()
    resp = instance.create(data=data)
    return {"string": resp}

@router.post("/test-post/")
async def test_post(request_body: dict):
    return request_body


@router.put("/sample-crud/{string_id}", tags=["sample-crud"], status_code=status.HTTP_202_ACCEPTED)
async def update_string(string_id: int, data: dict):
    """
    Update a string with the given ID.
    """
    instance = MySqlRepository()
    resp = instance.update(id=string_id, data=data)
    return {"status": "updated", "status_code": status.HTTP_202_ACCEPTED}


@router.delete("/sample-crud/{string_id}",tags=["sample-crud"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_string(string_id: int):
    """
    Delete a string with the given ID.
    """
    instance = MySqlRepository()
    instance.delete(id=string_id)
    return {"status": "deleted", "status_code": status.HTTP_204_NO_CONTENT}
