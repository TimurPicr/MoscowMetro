from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from bot.keyboards.choose_station import create_inline_keyboard, NLPCallback
from bot.nlp.nlp_model import nlp_request, get_flow_on_date, get_flow_on_period

router = Router()


@router.message(F.text)
async def ans_message(message: Message):
    ans_from_nlp = nlp_request(message.text, message.date.date())
    if type(ans_from_nlp['station']) == str:  # station is definite
        if ans_from_nlp['date']['type'] == 'day':  # date is a specific day
            await message.answer(get_flow_on_date({'station': ans_from_nlp['station'],
                                                   'date': ans_from_nlp['date']['date']}))
        elif ans_from_nlp['date']['type'] == 'period':  # date is list of possible stations
            await message.answer(get_flow_on_period({'station': ans_from_nlp['station'],
                                                     'date': ans_from_nlp['date']['date']}))
    elif type(ans_from_nlp['station']) == list:  # station needs to be chosen
        await message.answer('Уточните, пожалуйста, какая именно станция вас интересует:',
                             reply_markup=create_inline_keyboard(ans_from_nlp).as_markup())


@router.callback_query(NLPCallback.filter(F.datetype == "day"))
async def flow_on_day(query: CallbackQuery, callback_data: NLPCallback):
    flow = get_flow_on_date({'station': callback_data.station,
                             'date': callback_data.date})
    await query.message.answer(f'Станция: {callback_data.station}\n'
                               f'Дата: {callback_data.date}\n'
                               f'Нагрузка: {flow}')
    await query.message.delete()


@router.callback_query(NLPCallback.filter(F.datetype == "period"))
async def flow_on_period(callback: CallbackQuery, callback_data: NLPCallback):
    flow = get_flow_on_period({'station': callback_data.station,
                               'date': callback_data.date})
    await callback.message.answer(f'Станция: {callback_data.station}\n'
                                  f'Дата: {callback_data.date}\n'
                                  f'Нагрузка: {flow}')
    await callback.message.delete()  # params = {'text': 'hello', 'today': '2021-10-10'}
