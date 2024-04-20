import hors
import datetime


def find_date(text_message: str, today_date: datetime.datetime):
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