from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Кинуть смачный кул 🆒🆒🆒')],
    [KeyboardButton(text='Сдать матан 😍'), KeyboardButton(text='Пипипупу 🙌')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню:')
