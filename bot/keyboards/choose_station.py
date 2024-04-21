import datetime
from typing import List, Tuple

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class NLPCallback(CallbackData, prefix="models"):
    station: str | List[str]
    datetype: str
    date: datetime.date | Tuple[datetime.date]


def create_inline_keyboard(ans_from_nlp):
    builder = InlineKeyboardBuilder()
    for station in ans_from_nlp['station']:
        builder.button(text=station, callback_data=NLPCallback(station=station, datetype=ans_from_nlp['date']['type'],
                                                               date=ans_from_nlp['date']['date']).pack())
    builder.adjust(2)
    return builder
