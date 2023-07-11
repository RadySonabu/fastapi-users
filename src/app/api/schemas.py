import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    tenant: str


class UserCreate(schemas.BaseUserCreate):
    tenant: str


class UserUpdate(schemas.BaseUserUpdate):
    tenant: str
