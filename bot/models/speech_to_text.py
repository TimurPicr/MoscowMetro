import glob
import io

from vosk import Model, KaldiRecognizer, SetLogLevel
import json

from aiogram import Bot
from aiogram.types import Voice
from pydub import AudioSegment
import os

from bot.config import PATH_TO_PROJECT

SetLogLevel(0)
FRAME_RATE = 16000
CHANNELS = 1
model = Model(PATH_TO_PROJECT + '\models\model')


async def save_voice_as_mp3(bot: Bot, voice: Voice) -> str:
    """
    Use to download user's audio message in.mp3 format

    :param bot: Telegram bot object
    :param voice: User's voice message
    :return: Absolute path to saved ".\bot\cache\voice.mp3"
    """
    # downloading voice from chat

    voice_file_info = await bot.get_file(voice.file_id)
    voice_ogg = io.BytesIO()
    await bot.download_file(voice_file_info.file_path, voice_ogg)
    voice_mp3_path = f"{PATH_TO_PROJECT}\models\cache\\voice.mp3"
    print(voice_mp3_path)
    AudioSegment.from_file(voice_ogg, format="ogg").export(voice_mp3_path, format="mp3")
    return voice_mp3_path


async def audio_to_text(file_path: str) -> str:
    """
    Use to convert audio.mp3 to raw russian text
    :param file_path: Absolute path to audio.mp3
    :return: Raw russian text
    """
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    # preprocessing audio for recognition
    mp3 = AudioSegment.from_mp3(file_path)
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)

    rec.AcceptWaveform(mp3.raw_data)
    result = rec.Result()
    print(json.loads(result)["text"])

    return json.loads(result)["text"]
