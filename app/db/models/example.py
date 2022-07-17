from db.models.common import TimestampModel, UUIDModel


class Example(TimestampModel, UUIDModel, table=True):
    __tablename__ = "example"

    name: str
    active: bool = True

    def __repr__(self):
        return f"<Example (id: {self.id})>"
