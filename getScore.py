import requests
import datetime


def beastScore():
    week = getCurrentWeek()
    if week == 0:
        return "Couch check-ins will start after the first week"
    html = f'https://api.sleeper.app/v1/league/727263507439001600/matchups/{week}'
    source = requests.get(html).json()
    for team in source:
        if team['roster_id'] == 3:
            matchup = team['matchup_id']
            beastpoints = team['points']
    for team in source:
        if team['matchup_id'] == matchup and team['roster_id'] != 3:
            rivalpoints = team['points']
    if rivalpoints > beastpoints:
        response = ':cry: Marco on the couch this week :cry:'
    else:
        response = ':bed: The Beastie bed is warm this week :bed:'
    return response

def getCurrentWeek():
    today = datetime.datetime.now().date()
    if today < datetime.date(2021, 9, 14):
        return 0
    elif today < datetime.date(2021, 9, 21):
        return 1
    elif today < datetime.date(2021, 9, 28):
        return 2
    elif today < datetime.date(2021, 10, 5):
        return 3
    elif today < datetime.date(2021, 10, 12):
        return 4
    elif today < datetime.date(2021, 10, 19):
        return 5
    elif today < datetime.date(2021, 10, 26):
        return 6
    elif today < datetime.date(2021, 11, 2):
        return 7
    elif today < datetime.date(2021, 11, 9):
        return 8
    elif today < datetime.date(2021, 11, 16):
        return 9
    elif today < datetime.date(2021, 11, 23):
        return 10
    elif today < datetime.date(2021, 11, 30):
        return 11
    elif today < datetime.date(2021, 12, 7):
        return 12
    else:
        return 13
