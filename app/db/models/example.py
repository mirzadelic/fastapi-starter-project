from sqlmodel import Field, SQLModel


class ExampleBase(SQLModel):
    name: str
    active: bool = True


class Example(ExampleBase, table=True):
    __tablename__ = 'example'

    id: int = Field(default=None, primary_key=True)

    def __repr__(self):
        return f'<Example (id: {self.id})>'
