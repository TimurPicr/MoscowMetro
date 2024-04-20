import datetime
from typing import Dict, Union, Tuple, List

import hors
import pandas as pd
from fuzzywuzzy import fuzz

from bot.config import PATH_TO_PROJECT

df = pd.read_excel(PATH_TO_PROJECT + '/flow_data.xlsx')
stations = df['Станция'].unique()


# st - станция из списка
def find_station(stations, str):  # stations = df['Станция'].unique()
    ans = []

    # Обрабатываем входную строку
    s = str.lower().split()[0]
    str = str.lower()
    new_str = ''
    for i in str:
        if i not in [',', '.', ':', ';']:  # Дополнить
            new_str += i
    str = new_str.split()
    new_str = []
    for i in str:
        if len(i) >= 4:
            new_str.append(i)
    str = new_str

    # Ищем совпадения
    max = 0
    word = ''
    for st in stations:
        new_st = st.lower().split()[0]
        for i in range(len(str)):
            var = fuzz.ratio(new_st, str[i])
            if (var >= 85):  # Настраиваем
                ans.append(st)
            if (var >= max):
                max = var
                word = st
    if len(ans) == 0:
        return word
    elif len(ans) == 1:
        return ans[0]
    else:
        return ans


def find_date(text_message: str, today_date: datetime.datetime) -> dict:
    if '1905 года' in text_message:
        text_message.replace('1905 года ', '')
    r = hors.process_phrase(text_message, now=today_date)
    res = dict()
    a = r.dates[0].date_from.date()
    b = r.dates[0].date_to.date()
    if a == b:
        res['type'] = 'day'
        res['date'] = a
    else:
        res['type'] = 'period'
        res['date'] = (a, b)
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
    date_dt = pd.to_datetime([str(keys['date'])])
    ans = (df.loc[(df['Станция'] == keys['station'])])
    return str(ans[date_dt].values[0][0])


def get_flow_on_period(keys: Dict[str, Union[str, Tuple[datetime.datetime]]]) -> str:
    """
    Use this method to get flow on a period of time

    :param keys: Dictionary consists of specific station and date period in type: Tuple[datetime.date]
    :return: Flow on specific date in string format
    """
    date_dt1 = "2024-01-03"
    date_dt2 = "2024-01-08"
    ans = (df.loc[(df['Станция'] == keys['station'])])
    return str(ans.loc[date_dt1:date_dt2, 'Количество пассажиров'].sum())

    # саня отправит
    # ans = (df.loc[(df['Станция'] == keys['station'])])
    # return str(ans[date_dt1].values[0][0])
