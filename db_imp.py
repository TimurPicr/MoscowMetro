import pandas as pd

from bot.config import PATH_TO_PROJECT


def get_index(station, df):
    return df.loc[df['Станция'] == station].index[0]


def del_station(station, first_val, df):
    return df[~((df['Станция'] == station) & (df.iloc[:, 3] == first_val))]


def rename_station(station, new_name, df):
    df.loc[get_index(station, df), 'Станция'] = new_name


df = pd.read_excel(f'{PATH_TO_PROJECT}\\flow_data.xlsx')

rename_station('Андроновка МЦК', 'Андроновка', df)
rename_station('Балтийская МЦК', 'Балтийская', df)
rename_station('Белокаменная МЦК', 'Белокаменная', df)
rename_station('ЗИЛ МЦК', 'Завод им. Лихачёва', df)
rename_station('Зорге МЦК', 'Зорге', df)
rename_station('Измайлово МЦК', 'Измайлово', df)
rename_station('Коптево МЦК', 'Коптево', df)
rename_station('Крымская МЦК', 'Крымская', df)
rename_station('Лихоборы МЦК', 'Лихоборы', df)
rename_station('Локомотив МЦК', 'Локомотив', df)
rename_station('Лужники МЦК', 'Лужники', df)
rename_station('Москва-Сити МЦК', 'Москва-Сити', df)
rename_station('Панфиловская МЦК', 'Панфиловская', df)
rename_station('Пл. Гагарина МЦК', 'Пл. Гагарина', df)
rename_station('Ростокино МЦК', 'Ростокино', df)
rename_station('Угрешская МЦК', 'Угрешская', df)
rename_station('Стрешнево МЦК', 'Стрешнево', df)
rename_station('Хорошёво МЦК', 'Хорошёво', df)

rename_station('Автозавод. МЦК', 'Автозаводская МЦК', df)
rename_station('Б-р Рокоссов.МЦК', 'Б-р Рокоссовского МЦК', df)
rename_station('Ботан. сад МЦК', 'Ботанический сад МЦК', df)
rename_station('Верхн. Котлы МЦК', 'Верхние Котлы МЦК', df)
rename_station('Нижегородск. МЦК', 'Нижегородская МЦК', df)
rename_station('Новохохлов-я МЦК', 'Новохохловская МЦК', df)
rename_station('Сокол. гора МЦК', 'Соколиная Гора МЦК', df)
rename_station('Шоссе энтуз.МЦК', 'Шоссе Энтузиастов МЦК', df)

rename_station('Авиамотор-я КалЛ', 'Авиамоторная КАЛ', df)
df = del_station('Авиамоторная БКЛ', 6787, df)
rename_station('Авиамоторная нек', 'Авиамоторная НЕК', df)
rename_station('Автозаводская', 'Автозаводская ЗЛ', df)
rename_station('Александр. сад', 'Александровский сад', df)
rename_station('Б-р Адм. Ушакова', 'Б-р Адмирала Ушакова', df)
rename_station('Б-р Дм. Донского', 'Б-р Дмитрия Донского', df)
rename_station('Б.Рокоссовского', 'Б-р Рокоссовского СОК', df)
rename_station('Библ. им. Ленина', 'Библиотека им. Ленина', df)
rename_station('Ботанический сад', 'Ботанический сад КРЛ', df)
rename_station('Владыкино', 'Владыкино СТМ', df)
rename_station('Волгоградский пр', 'Волгоградский пр-кт', df)
df = del_station('Воробьевы горы С', 14559, df)
df = del_station('Воробьевы горы С', 8408, df)
df = del_station('Выхино 2', 3331, df)
rename_station('Дел. центр БКЛ', 'Деловой центр БКЛ', df)
rename_station('Дел. центр СолЛ', 'Деловой центр СОЛ', df)
rename_station('Дубровка', 'Дубровка ЛЮБ', df)
df = del_station('К', 18248, df)
df = del_station('Каширская', 5708, df)
rename_station('Каширская', 'Каширская БКЛ', df)
rename_station('Каширская (Зам)', 'Каширская ЗЛ', df)
rename_station('Каширская (Ках.)', 'Каширская КАХ', df)
rename_station('Киевская (Фил.)', 'Киевская ФЛ', df)
rename_station('Китай-город(Т-К)', 'Китай-город ТКР', df)
rename_station('Комсомольск. СЛ', 'Комсомольская СОК', df)
df = del_station('Комсомольская КЛ', 16101, df)
rename_station('Комсомольская 2', 'Комсомольская КЛ', df)
rename_station('Красногвардейск.', 'Красногвардейская', df)
rename_station('Краснопресненск.', 'Краснопресненская', df)
rename_station('Крест. застава', 'Крестьянская Застава', df)
rename_station('Ленинский пр-т', 'Ленинский пр-кт', df)
rename_station('Лермонтовский пр', 'Лермонтовский пр-кт', df)
df = del_station('Лефортово', 6699, df)
rename_station('Лефортово нек.', 'Лефортово НЕК', df)
rename_station('Ломоносов-ий п-т', 'Ломоносовский пр-кт КАЛ', df)
rename_station('Ломоносовск.пр-т', 'Ломоносовский пр-кт СОЛ', df)
rename_station('Марьина Роща ЛДЛ', 'Марьина Роща ЛЮБ', df)
rename_station('Мичурин.пр-т БКЛ', 'Мичуринский пр-кт БКЛ', df)
rename_station('Мичурин.пр-тСолЛ', 'Мичуринский пр-кт СОЛ', df)
rename_station('Нагатинский З-н', 'Нагатинский Затон', df)
rename_station('Народное Ополч-е', 'Народное Ополчение', df)

rename_station('Нахимовский пр-т', 'Нахимовский пр-кт', df)
rename_station('Нижегород-я БКЛ', 'Нижегородская БКЛ', df)
rename_station('Нижегород-я НБС', 'Нижегородская НЕК', df)
df = del_station('Нижегородская', 7107, df)
rename_station('Окружная', 'Окружная ЛЮБ', df)
df = del_station('Парк Победы КС', 1677, df)
rename_station('Парк Победы СолЛ', 'Парк Победы СОЛ', df)
rename_station('Парк культуры СЛ', 'Парк культуры СОК', df)
rename_station('Петр.-Разумовск.', 'Петровско-Разумовская СТМ', df)
rename_station('Петровско-Разум.', 'Петровско-Разумовская ЛЮБ', df)
rename_station('Петр.парк(Солнц)', 'Петровский парк СОЛ', df)
rename_station('Петровский парк', 'Петровский парк БКЛ', df)
rename_station('Печатники ЛДЛ', 'Печатники ЛЮБ', df)
rename_station('Площадь Ильича', 'Пл. Ильича', df)
rename_station('Пр-т Вернад. БКЛ', 'Пр-кт Вернадского БКЛ', df)
rename_station('Пр-т Вернадск.СЛ', 'Пр-кт Вернадского СОК', df)
rename_station('Преображенск. пл', 'Преображенская пл.', df)
rename_station('Проспект Мира КЛ', 'Пр-кт Мира КЛ', df)
rename_station('Рижская', 'Рижская КРЛ', df)
rename_station('Рязанский пр-т', 'Рязанский пр-кт', df)
rename_station('Славянский бульв', 'Славянский б-р', df)
rename_station('Сокольники СЛ', 'Сокольники СОК', df)
df = del_station('Стенд', 5690, df)
rename_station('Таганская ТКЛ', 'Таганская ТКР', df)
rename_station('Театральная(Зам)', 'Театральная', df)
df = del_station('Текстильщики БКЛ', 2595, df)
rename_station('Текстильщики СЦ', 'Текстильщики БКЛ', df)
rename_station('Текстильщики ТКЛ', 'Текстильщики ТКР', df)
rename_station('Третьяковск. КРЛ', 'Третьяковская КРЛ', df)
rename_station('Третьяковск.КалЛ', 'Третьяковская КАЛ', df)
rename_station('Ул. Ак. Янгеля', 'Ул. Академика Янгеля', df)
rename_station('Ул.Дмитриевского', 'Ул. Дмитриевского', df)
rename_station('Улица 1905 года', 'Ул. 1905 года', df)
rename_station('Хорошев-я(Солнц)', 'Хорошёвская СОЛ', df)
df = del_station('Хорошёвская', 6138, df)
rename_station('Хорошёвская(Мн)', 'Хорошёвская БКЛ', df)
rename_station('ЦСКА', 'ЦСКА БКЛ', df)
rename_station('ЦСКА(Солнц.)', 'ЦСКА СОЛ', df)
rename_station('Ш. Энтузиастов', 'Шоссе Энтузиастов', df)
rename_station('Шелепиха', 'Шелепиха БКЛ', df)
rename_station('Шелепиха(Солнц.)', 'Шелепиха СОЛ', df)
rename_station('Электрозав-я АПЛ', 'Электрозаводская АПЛ', df)
rename_station('Электрозав-я БКЛ', 'Электрозаводская БКЛ', df)
rename_station('Электрозав-я нек', 'Электрозаводская НЕК', df)
rename_station('Юго-западная', 'Юго-Западная', df)
