import asyncio

from aiogram import Bot, Dispatcher

from bot.handlers.commands import router as base_commands_router
from bot.handlers.to_nlpmodel import router as to_nlpmodel_router
from bot.config import TOKEN
import logging

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(base_commands_router)
    dp.include_router(to_nlpmodel_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
