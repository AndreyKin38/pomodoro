from pydantic import BaseModel, Field, model_validator


class TaskSchema(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int  # = Field(exclude=True)

    class Config:
        from_attributes = True

    @model_validator(mode="after")
    def check_value(self):
        if self.name is None and self.pomodoro_count is None:
            raise ValueError("name or pomodoro_count must be provided")
        return self



