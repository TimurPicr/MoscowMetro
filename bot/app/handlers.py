from aiogram import Router
from aiogram.types import Message

import aiohttp

router = Router()


@router.message()
async def echo(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/') as response:
            html = await response.text()
    await message.answer(message.text + html)
