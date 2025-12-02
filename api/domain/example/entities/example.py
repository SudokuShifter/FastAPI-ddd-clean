from pydantic import BaseModel, Field


class ExampleModel(BaseModel):
    first_field: str
    second_field: str


class ExampleModelResponse(BaseModel):
    result: str
