import asyncio
from typing import Any

import aiohttp
import structlog
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse

log = structlog.get_logger()


def send_data(data: Any, status_code: int = 200):
    return ORJSONResponse(
        status_code=status_code,
        content={
            "data": jsonable_encoder(data),
        },
    )


def send_info(info: str, status_code: int = 200):
    return ORJSONResponse(
        status_code=status_code,
        content={
            "info": info,
        },
    )


def client_side_error(detail: str, status_code: int = 400):
    log.error(detail)
    return HTTPException(
        status_code=status_code,
        detail=detail,
    )


def internal_server_error(detail: str, status_code: int = 500):
    log.error(detail)
    return HTTPException(
        status_code=status_code,
        detail=detail,
    )


async def aiohttp_post(url: str, data: Any = None):
    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.post(url=url, data=data) as response:
            return await response.json(), response.status
