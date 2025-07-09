from pydantic import BaseModel, Field, ConfigDict


class ReviewBase(BaseModel):
    text: str
    sentiment: str


class ReviewFullRead(ReviewBase):
    id: int
    created_at: str = Field(..., example="2025-07-09T14:20:00.123456")

    model_config = ConfigDict(from_attributes=True)
