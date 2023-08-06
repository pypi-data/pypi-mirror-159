from __future__ import annotations
from enum import Enum
from typing import List, Optional, Sequence, Type, Any, TypeVar, Dict
from abc import ABC
from pydantic import BaseModel, root_validator, create_model, Extra
from fastapi.security.base import SecurityBase


TBaseModel = TypeVar('TBaseModel', bound=BaseModel)
TCreateModel = TypeVar('TCreateModel', bound=BaseModel)
TUpdateModel = TypeVar('TUpdateModel', bound=BaseModel)


class Method(Enum):
    GET_LIST = 'list'
    GET_AGGREGATE = 'aggregate'
    GET = 'get'
    POST = 'post'
    PATCH = 'patch'
    PUT = 'put'
    DELETE = 'delete'


class RouterSchema(BaseModel, arbitrary_types_allowed=True, extra=Extra.allow):
    name: str
    list: Type[BaseModel]
    get: Type[TBaseModel]
    create: Optional[Type[TCreateModel]] = None
    create_multi: bool = False
    update: Optional[Type[TUpdateModel]] = None
    delete: bool = True
    children: List[RouterSchema] = []
    parent: Optional[RouterSchema] = None
    security: Optional[SecurityBase] = None
    security_scopes: Optional[Dict[Method, Sequence[str]]] = None

    @root_validator(pre=True)
    def _init_list(cls, values: dict):
        if not values.get('list'):
            values['list'] = create_model(f"{values['get'].__qualname__}List", __module__=values['get'].__module__, items=(List[values['get']], ...))

        return values

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

        for child in self.children:
            child.parent = self


RouterSchema.update_forward_refs()


class BaseRouter(ABC):
    pass
