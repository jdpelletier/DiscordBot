import requests
import datetime


def beastScore(sender):
    print(sender)
    print(sender.name)
    print(sender == "jpelle420#5069")
    print(sender.name == "jpelle420#5069")
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
    if rivalpoints == 0 and beastpoints == 0 and sender == "jpelle420#5069":
        response =  "Place your bets for a warm bed :bed: or a cold couch :couch: this week."
    elif rivalpoints == 0 and beastpoints == 0 and sender != "jpelle420#5069":
        response = "The week hasn't started for the boys yet, place your bets on jpelle's post."
    elif rivalpoints > beastpoints and ongoingWeek():
        response = ":pray: Pray for Marco :pray:"
    elif rivalpoints > beastpoints and (ongoingWeek() == False):
        response = ':cry: Marco on the couch this week :cry:'
    elif rivalpoints < beastpoints and ongoingWeek():
        response = ":clinking_glass: Jacob should prepare the special occasion sheets :clinking_glass:"
    else:
        response = ':bed: The Beastie bed is warm this week :bed:'
    return response

def getCurrentWeek():
    today = datetime.datetime.now().date()
    if today < datetime.date(2021, 9, 9):
        return 0
    elif today < datetime.date(2021, 9, 16):
        return 1
    elif today < datetime.date(2021, 9, 23):
        return 2
    elif today < datetime.date(2021, 9, 30):
        return 3
    elif today < datetime.date(2021, 10, 7):
        return 4
    elif today < datetime.date(2021, 10, 14):
        return 5
    elif today < datetime.date(2021, 10, 21):
        return 6
    elif today < datetime.date(2021, 10, 28):
        return 7
    elif today < datetime.date(2021, 11, 4):
        return 8
    elif today < datetime.date(2021, 11, 11):
        return 9
    elif today < datetime.date(2021, 11, 18):
        return 10
    elif today < datetime.date(2021, 11, 25):
        return 11
    elif today < datetime.date(2021, 12, 2):
        return 12
    else:
        return 13

def ongoingWeek():
    dow = datetime.datetime.today().weekday()
    if dow > 2:
        return True
    elif (dow == 0) and (datetime.datetime.today().time() < datetime.time(17, 0, 0)):
        return True
    else:
        return False
