from api.domain.example.entities.example import ExampleModel
from api.infrastructure.database.postgres import PostgresPool


class ExampleRepository:
    def __init__(self, db: PostgresPool):
        self.db = db

    async def some_method(self) -> None:
        query = """
            SELECT * FROM "SomeTable"
        """
        raw_data = self.db.pool.execute(query)
        return [ExampleModel(**row) for row in raw_data]
