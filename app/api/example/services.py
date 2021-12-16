from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from db.models.example import Example, ExampleBase


class ExampleService:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def get_all_examples(self) -> List[Example]:
        examples = await self.session.execute(select(Example))

        return examples.scalars().fetchall()

    async def create_example(self, data: ExampleBase) -> Example:
        example = Example(**data.dict())
        self.session.add(example)
        await self.session.commit()
        await self.session.refresh(example)

        return example
