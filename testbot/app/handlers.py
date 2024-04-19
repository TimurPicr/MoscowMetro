from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! Ваш ID: {message.from_user.id}, имя: {message.from_user.first_name}',
                        reply_markup=kb.main)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')


@router.message(F.text == 'Кинуть смачный кул 🆒🆒🆒')
async def throw_cool(message: Message):
    await message.answer('🆒')


@router.message(F.text == 'Сдать матан 😍')
async def sday_ege(message: Message):
    await message.answer('Рано еще, сессия не скоро')


@router.message(F.text == 'Пипипупу 🙌')
async def pipipupu(message: Message):
    await message.answer('https://youtu.be/5wMO5_yHml0?si=BhqxU3ssLHV8ccH7')


# @router.message(Command('get_photo'))
# async def get_photo(message: Message):
#     await message.answer_photo(photo='AgACAgIAAxkBAAMSZiJJakJSQDTIWa_ae6JYSqAmvFIAAi_dMRsPoxBJqBV-Z67pMZgBAAMCAAN5AAM0BA',
#                                caption='иди нахуй')
