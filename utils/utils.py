import importlib
import inspect
import json
import uuid
from typing import List, Callable

from sqlalchemy_utils import Ltree

from schemas.active_action import ActiveActionPath


def nlevel(path: Ltree) -> int:
    return len(path.path.split("."))


def uuid_to_ltree(object: uuid.UUID) -> Ltree:
    uuid_parts = str(object).replace("-", "_").split("_")
    ltree = ".".join(uuid_parts)

    return Ltree(ltree)


def list_to_ltree(objects: List[str]) -> Ltree:
    result = Ltree(objects[0])
    for obj in objects[1:]:
        result += Ltree(obj)

    return result


def string_path_to_json(paths: list[str]):
    return [json.loads(path) if not isinstance(path, dict) else path for path in paths]


def import_func(package: str, func: str) -> Callable:
    module = importlib.import_module(package)
    function = getattr(module, func)

    return function


async def run_func(func: callable, *args, **kwargs) -> None:
    if inspect.iscoroutinefunction(func):
        return await func(*args, **kwargs)
    return func(*args, **kwargs)


def get_path(paths: list[ActiveActionPath], id: uuid.UUID) -> ActiveActionPath | None:
    for path in paths:
        if path.node_id == id:
            return path

    return None
