from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

import aiohttp

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет, я бот МосТрансПроекта! Я могу выдавать информацию о пассажиропотоке на станциях "
                         "метро, принимая запросы в свободной форме!")


# @router.message(Command("help"))
# async def start(message: Message):
#     await message.answer("Привет, я бот МосТрансПроекта! Я могу выдавать информацию о пассажиропотоке на станциях "
#                          "метро, принимая запросы в свободной форме!")
