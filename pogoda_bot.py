#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import sys
from datetime import datetime
import json

# для запуска необходимо:
# 1. Получить и указать API-ключ Яндекс-погоды (headers)
# 2. Указать широту и долготу (координаты) (pogoda)
# 3. Указать api_token телеграм вместо XXXXXX (api_token)
# 4. Указать api_token телеграм вместо XXXXXX (requests.get)
# 5. Указать chat_id



headers = {"API-ключ Яндекс-погоды"}
pogoda = requests.get(url="https://api.weather.yandex.ru/v2/informers?lat=ШИРОТА&lon=ДОЛГОТА&lang=ru_RU", headers = headers)
b = pogoda.json()


# расшифровка осадков
osad = {'clear': 'ясно', 'partly-cloudy': 'малооблачно', 'cloudy': 'облачно с прояснениями', 'overcast': 'пасмурно',
       'drizzle': 'морось', 'light-rain': 'небольшой дождь', 'rain': 'дождь', 'moderate-rain': 'умеренно сильный дождь',
       'heavy-rain': 'сильный дождь', 'continuous-heavy-rain': 'длительный сильный дождь', 'showers': 'ливень',
       'wet-snow': 'дождь со снегом', 'light-snow': 'небольшой снег', 'snow': 'снег', 'snow-showers': 'снегопад',
       'hail': 'град', 'thunderstorm': 'гроза', 'thunderstorm-with-rain': 'дождь с грозой', 'thunderstorm-with-hail': 'гроза с градом'}

wind = {'nw': 'северо-западное', 'n': 'северное', 'ne': 'северо-восточное', 'e': 'восточное', 'se': 'юго-восточное',
's': 'южное', 'sw': 'юго-западное', 'w': 'западное', 'c': 'штиль'}

part_day = {'day': 'Днем', 'evening': 'Вечером', 'night': 'Ночью', 'morning': 'Утром'}


fore0 = part_day[b['forecast']['parts'][0]['part_name']] + ' темп: ' + str(b['forecast']['parts'][0]['temp_avg']) + ' как ' + str(b['forecast']['parts'][0]['feels_like']) + ', ветер: ' + str(b['forecast']['parts'][0]['wind_speed']) + 'м/с, ' + wind[b['forecast']['parts'][0]['wind_dir']] + ', ' + osad[b['forecast']['parts'][0]['condition']] + ', давление: ' + str(b['forecast']['parts'][0]['pressure_mm']) + ' мм рт.ст., ' + 'влажность: ' + str(b['forecast']['parts'][0]['humidity']) + '%' + ', вероятность осадков: ' + str(b['forecast']['parts'][0]['prec_prob']) + '%';
fore1 = part_day[b['forecast']['parts'][1]['part_name']] + ' темп: ' + str(b['forecast']['parts'][1]['temp_avg']) + ' как ' + str(b['forecast']['parts'][1]['feels_like']) + ', ветер: ' + str(b['forecast']['parts'][1]['wind_speed']) + 'м/с, ' + wind[b['forecast']['parts'][1]['wind_dir']] + ', ' + osad[b['forecast']['parts'][1]['condition']] + ', давление: ' + str(b['forecast']['parts'][1]['pressure_mm']) + ' мм рт.ст., ' + 'влажность: ' + str(b['forecast']['parts'][1]['humidity']) + '%' + ', вероятность осадков: ' + str(b['forecast']['parts'][1]['prec_prob']) + '%';

# текст для отправки в телеграм
text = 'Сейчас темп: ' + str(b['fact']['temp']) + ' как ' + str(b['fact']['feels_like']) + ', ветер: ' + str(b['fact']['wind_speed']) + 'м/с, ' + wind[b['fact']['wind_dir']] + ', ' + osad[b['fact']['condition']] + ', давление: ' + str(b['fact']['pressure_mm']) + ' мм рт.ст., ' + 'влажность: ' + str(b['fact']['humidity']) + '%' + '\n\n' + fore0 + '\n\n' + fore1;

# текст для вывода в лог-файл
text2 = str(b['now_dt']) +'; Темп: ' + str(b['fact']['temp']) + ', как ' + str(b['fact']['feels_like']) + '; Давление: ' + str(b['fact']['pressure_mm']) + ' мм рт.ст.; ' + 'Влажность: ' + str(b['fact']['humidity']) + '%; ' + osad[b['fact']['condition']] + '; ветер:' + str(b['fact']['wind_speed']) + 'м/с, направление: ' + wind[b['fact']['wind_dir']];


# отправка в телеграм
api_token = 'XXXXXX'
requests.get('https://api.telegram.org/botXXXXXX/sendMessage'.format(api_token), params=dict(
   chat_id='чат_ИД',
   text=text
))


#print(text2)
