import asyncio
import time

import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()


class GigachatRequest(BaseModel):
    text: str
    today: date


def request_to_giga(text):
    return text


@app.get("/")
def ping_pong():
    print('pong')
    return 'ok'


def conv_with_db(json):
    pass


@app.get('/conversation/')
async def send_to_gigachat(text: str, today: date):
    json = request_to_giga(text)
    return json
