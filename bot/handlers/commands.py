from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

commands = ("/start - приветствие\n"
            "/help - список команд бота\n"
            "/give_busiest_line - вывод заданного количества наиболее загруженных линий за период\n"
            "/give_busiest_station - вывод заданного количества наиболее загруженных станций за период")


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет, я бот МосТрансПроекта! Я могу выдавать информацию о пассажиропотоке на станциях "
                         "метро, принимая запросы в свободной форме!")


@router.message(Command("help"))
async def help(message: Message):
    await message.answer(commands)


@router.message(Command("give_busiest_line"))
async def give_busiest_line(message: Message):
    await message.answer(commands)


@router.message(Command("give_busiest_station"))
async def give_busiest_line(message: Message):
    await message.answer(commands)