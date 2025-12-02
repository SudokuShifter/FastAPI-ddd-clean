from pydantic import BaseModel, Field
from fastapi import Form


class ExampleRequest(BaseModel):
    first_field: str = Form(..., description="Some Field")
    second_field: int = Form(..., description="Some Field")


class ExampleRequestTwo(BaseModel):
    first_field: str = Field(..., description="Some Field")
    second_field: str = Field(..., description="Some Field")
