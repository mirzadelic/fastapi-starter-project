from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.example.services import ExampleService
from db.db import get_session
from db.models.example import Example, ExampleBase

router = APIRouter()


@router.get("/", response_model=list[Example])
async def get_examples(session: AsyncSession = Depends(get_session)) -> list[Example]:
    example_service = ExampleService(session=session)
    return await example_service.get_all_examples()


@router.post("/", response_model=Example)
async def create_example(
    data: ExampleBase,
    session: AsyncSession = Depends(get_session),
) -> Example:
    example_service = ExampleService(session=session)
    example = await example_service.create_example(data)
    return example
