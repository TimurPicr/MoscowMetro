import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.handlers.commands import router as commands_router
from bot.handlers.text_to_flow import router as to_nlp_router
from bot.handlers.speech_to_flow import router as from_audio_router
import bot.models.speech_to_text  # to initialize audio module
from bot.config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(commands_router, to_nlp_router, from_audio_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
