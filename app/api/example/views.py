from typing import List

from api.example.services import ExampleService
from db.db import get_session
from db.models.example import Example, ExampleBase
from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/", response_model=List[Example])
async def get_examples(example_service: ExampleService = Depends()) -> List[Example]:
    return await example_service.get_all_examples()


@router.post("/", response_model=Example)
async def create_example(
    data: ExampleBase,
    example_service: ExampleService = Depends()
) -> Example:
    example = await example_service.create_example(data)
    return example
