import asyncio

from aiogram import Bot, Dispatcher

from bot.app.handlers import router
from bot.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
