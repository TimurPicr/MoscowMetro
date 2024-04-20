import asyncio

from aiogram import Bot, Dispatcher

from bot.handlers.commands import router as commands_router
from bot.handlers.to_nlp import router as to_nlp_router
from bot.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(commands_router, to_nlp_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
