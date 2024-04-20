from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_inline_keyboard(ans_from_nlp):
    builder = InlineKeyboardBuilder()
    for station in ans_from_nlp['station']:
        builder.button(text=station, callback_data=station)
    builder.adjust(2)
    return builder

