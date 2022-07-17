from api.example.schemas import ExampleCreateSchema, ExampleSchema
from api.example.services import ExampleService
from db.db import db_session
from db.models.example import Example
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/", response_model=list[ExampleSchema])
async def get_examples(
    session: AsyncSession = Depends(db_session),
) -> list[Example]:
    example_service = ExampleService(session=session)
    return await example_service.get_all_examples()


@router.post("/", response_model=ExampleSchema)
async def create_example(
    data: ExampleCreateSchema,
    session: AsyncSession = Depends(db_session),
) -> Example:
    example_service = ExampleService(session=session)
    example = await example_service.create_example(data)
    return example
