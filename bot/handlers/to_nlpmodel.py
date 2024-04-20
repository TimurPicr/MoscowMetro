import datetime
from typing import Dict, Union, List

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import pandas as pd
import aiohttp
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.config import PATH_TO_PROJECT
from bot.handlers.keyboards import create_inline_keyboard
from bot.handlers.nlp_model import get_nameof_station

router = Router()
df = pd.read_excel(PATH_TO_PROJECT + '/flow_data.xlsx')
stations = df['Станция'].unique()


def get_station_past(keys: Dict[str, Union[str, datetime.datetime]]) -> str:
    date_dt = pd.to_datetime([str(keys['date'])])
    ans = (df.loc[(df['Станция'] == keys['station'])])
    return str(ans[date_dt].values[0][0])


def nlp_request(text: str, today: datetime.datetime) -> Dict[str, Union[str, datetime.datetime]]:
    station = get_nameof_station(stations, text)
    date = datetime.date(2024, 4, 3)
    # date = '2024-04-03'
    return {'station': station, 'date': date}


@router.message(F.text)
async def ans_on_nl(message: Message):
    ans_from_nlp = nlp_request(message.text, message.date)
    if type(ans_from_nlp['station']) == str:
        await message.answer(get_station_past(ans_from_nlp))
    elif type(ans_from_nlp['station']) == list:
        await message.answer("Select a station:", reply_markup=create_inline_keyboard(ans_from_nlp).as_markup())


@router.callback_query(F.data)
async def one_station_choose(callback: CallbackQuery):
    await callback.message.answer(get_station_past({'station': callback.data, 'date': datetime.date(2024, 4, 3)}))
    await callback.message.delete()    # params = {'text': 'hello', 'today': '2021-10-10'}
