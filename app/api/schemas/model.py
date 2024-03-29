from typing import Annotated
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class ModelBase(BaseModel):
    name: Annotated[str, Field(description="Model name")]
    description: Annotated[str, Field(description="Model description")]
    source_path: Annotated[str, Field(description="Path to the model source code")]
    status: Annotated[Status, Field(description="Model status")]
    image_tag: Annotated[str, Field(description="Docker image tag")]


class PutModel(ModelBase):
    created_by: Annotated[int, Field(description="User ID of the creator")]


class PatchModel(ModelBase):
    name: Annotated[str | None, Field(description="Model name")] = None
    description: Annotated[str | None, Field(description="Model description")] = None
    updated_by: Annotated[int, Field(description="User ID of the last updater")]
    source_path: Annotated[
        str | None, Field(description="Path to the model source code")
    ] = None
    status: Annotated[Status | None, Field(description="Model status")] = None
    image_tag: Annotated[str | None, Field(description="Docker image tag")] = None


class Model(ModelBase):
    id: Annotated[int, Field(description="Model ID")]
    created_by: Annotated[int, Field(description="User ID of the creator")]
    created_at: Annotated[datetime, Field(description="Creation date")]
    updated_by: Annotated[int, Field(description="User ID of the last updater")]
    updated_at: Annotated[datetime, Field(description="Last update date")]

    class Config:
        orm_mode = True


class ModelTest(BaseModel):
    id: Annotated[int, Field(description="ModelTest ID")]
    model_id: Annotated[int, Field(description="Model id")]
    user_id: Annotated[int, Field(description="User id")]
