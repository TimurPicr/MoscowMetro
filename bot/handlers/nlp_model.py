from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import hors
import datetime


# st - станция из списка
def get_nameof_station(stations, str): # stations = df['Станция'].unique()
    ans = []

    # Обрабатываем входную строку
    s = str.lower().split()[0]
    str = str.lower()
    new_str = ''
    for i in str:
        if i not in [',', '.', ':', ';']: # Дополнить
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
            if (var >= 85): # Настраиваем
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


def find_date(text_message: str, today: datetime.date) -> dict:
    r = hors.process_phrase(text_message)
    res = dict()
    match r.dates[0].type:
        case '<DateTimeTokenType.PERIOD: 2>':
            res['type'] = 'period'
            a = r.dates[0].date_from.date()
            b = r.dates[0].date_to.date()
            res['date'] = (a, b)
        case '<DateTimeTokenType.FIXED: 1>':
            res['type'] = 'day'
            a = r.dates[0].date_from.date()
            res['date'] = a
    return res