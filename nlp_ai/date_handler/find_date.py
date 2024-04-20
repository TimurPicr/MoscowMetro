import hors
import datetime


def find_date(text_message: str, today: datetime.date):
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
