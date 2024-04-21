import datetime
from typing import Dict, Union, Tuple, List

import hors
import pandas as pd
from fuzzywuzzy import fuzz
from words2numsrus import *

from bot.config import PATH_TO_PROJECT
from bot.models.predictor import LAST_DATE, predict
from db_imp import df

stations = df['Станция'].unique()


def parse_message(text: str) -> List[str]:
    """
    Use this method to make array of words from user`s message

    :param text: User`s message
    :return: Array of lowercase words from message without marks and excluded words
    """
    ban_marks = [',', '.', ':', ';', '?', '!', '#', '$', '%', '^', '&', '*', '/']
    ban_words = ['сколько', 'привет', 'через', 'после']
    text = text.lower()
    var = ''
    for symbol in text:
        if symbol not in ban_marks:
            var += symbol
    splitted_text = var.split()
    var = []
    for word in splitted_text:
        if (len(word) >= 4) and (word not in ban_words):
            var.append(word)
    return var


def parse_station(station: str) -> str:
    """
    Use this method to parse station name

    :param station: Name of station
    :return: Lowercase name of station without excluded words
    """
    ban_words = ['Б-р ', ' б-р', 'Пр-кт ', ' пр-кт', 'Пл. ', ' пл.', 'Ул. ', ' ул.', ' им.']
    for word in ban_words:
        if word in station:
            station = station.replace(word, '')
    return station.lower()


def find_station(stations: list[str], text: str) -> str | List[str]:
    """
    Use this method to find name of station in user`s message

    :param text: User`s message text
    :param stations: List of all station names
    :return: List of the most likely stations
    """
    ans = []
    best = 0
    best_station = ''
    for station in stations:
        for s in parse_message(text):
            var = fuzz.ratio(parse_station(station), s)
            if var >= 70:
                ans.append(station)
            if var >= best:
                best = var
                best_station = station
    if len(ans) == 0:
        return best_station
    elif len(ans) == 1:
        return ans[0]
    else:
        return ans


def find_date(text_message: str, today_date: datetime.datetime) \
        -> Dict[str, Union[str, datetime.date, Tuple[datetime.date]]]:
    """
    Use this method to find date data in user`s message

    :param text_message: User`s message text
    :param today_date: Date and time of user`s message
    :return: Dictionary with date type: fixed or period, and date data: datetime.date or Tuple[datetime.date]
    """
    if '1905 года' in text_message:
        text_message.replace('1905 года ', '')
    extractor = NumberExtractor()
    text_message = extractor.replace_groups(text_message)
    r = hors.process_phrase(text_message, now=today_date)
    res = dict()
    try:
        date_start = r.dates[0].date_from.date()
        date_end = r.dates[0].date_to.date()
        if date_start == date_end:
            res['type'] = 'day'
            res['date'] = date_start
        else:
            res['type'] = 'period'
            res['date'] = (date_start, date_end)

    except IndexError:
        res['type'] = 'noday'
        res['date'] = today_date.date()
    return res


def nlp_request(text: str, today: datetime.datetime) -> Dict[str, Union[str, List[str], Dict]]:
    """
    Use this method to process user's message to possible stations and target date

    :param text: Text of user's message
    :param today: Date and time of user's message
    :return: Dictionary: under 'station' list of stations or one station, under 'date' dict with data about timeframe
    """
    possible_station = find_station(stations, text)  # list of possible stations or one station
    date = find_date(text, today)  # {'type': 'day' or 'period', 'date': datetime.date or Tuple[datetime.date]}
    return {'station': possible_station, 'date': date}


def get_flow_on_date(keys: Dict[str, Union[str, datetime.date]]) -> str:
    """
    Use this method to get flow on a specific date

    :param keys: Dictionary consists of specific station and date in type: datetime.date
    :return: Flow on specific date in string format
    """
    if LAST_DATE >= keys['date']:
        date_dt = pd.to_datetime([str(keys['date'])])
        ans = (df.loc[(df['Станция'] == keys['station'])])
        return (f'Станция: {keys["station"]}\n'
                f'Дата: {keys["date"]}\n'
                f'Нагрузка: {ans[date_dt].values[0][0]}')
    else:
        distance = (keys['date'] - LAST_DATE).days
        ans = predict(keys["station"], df, time_left=distance)[0]
        return (f'Внимание, это предсказание!\n'
                f'Станция: {keys["station"]}\n'
                f'Дата: {keys["date"]}\n'
                f'Нагрузка: {ans}')


def get_flow_on_period(keys: Dict[str, Union[str, Tuple[datetime.datetime]]]) -> str:
    """
    Use this method to get flow on a period of time

    :param keys: Dictionary consists of specific station and date period in type: Tuple[datetime.date]
    :return: Flow on specific date in string format
    """
    date_dt1 = keys["date"][0]
    date_dt2 = keys["date"][1]

    if LAST_DATE >= keys['date'][0]:
        date_dt1 = keys["date"][0]
        date_dt2 = keys["date"][1]
        ans = (df.loc[(df['Станция'] == keys['station'])])
        return (f'Станция: {keys["station"]}\n'
                f'Период: с {date_dt1} по {date_dt2}\n'
                f'Нагрузка: {ans.loc[date_dt1:date_dt2, "Количество пассажиров"].sum()}')
    else:
        distance_left = (keys['date'] - LAST_DATE).days
        distance_right = (keys['date'] - LAST_DATE).days
        ans = predict(keys["station"], df, time_left=distance_left, time_right=distance_right).sum()
        return (f'Внимание, это предсказание!\n'
                f'Станция: {keys["station"]}\n'
                f'Дата: с {date_dt1} по {date_dt2}\n'
                f'Нагрузка: {ans}')
