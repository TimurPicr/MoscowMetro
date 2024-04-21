from aiogram import Router, F, Bot
from aiogram.types import Message

from bot.handlers.text_to_flow import process_message
from bot.models.speech_to_text import save_voice_as_mp3, audio_to_text

router = Router()


@router.message(F.content_type == "voice")
async def audio_to_flow(message: Message, bot: Bot):
    print('ok')
    voice_path = await save_voice_as_mp3(bot, message.voice)
    recognized_voice_text = await audio_to_text(voice_path)
    if recognized_voice_text:
        await process_message(recognized_voice_text, message.date, message)
    else:
        await message.answer('Не удалось распознать речь. Попробуйте еще раз.')
