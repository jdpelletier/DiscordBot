import requests
import os
import json


def getOdds():
    source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl").json()
    message = 'Bovada odds currently posted\n'
    data = source[0]
    for game in data:
        for team in data['events']:
            if len(message) > 1900:
                return message
            try:
                team_1 = team['competitors'][0]['name']
                team_2 = team['competitors'][1]['name']
                try: spread1 = team['displayGroups'][0]['markets'][0]['outcomes'][0]['price']['handicap']
                except KeyError: spread1 = None
                try: spread2 = team['displayGroups'][0]['markets'][0]['outcomes'][1]['price']['american']
                except KeyError: spread2 = None
                try: overunder = team['displayGroups'][0]['markets'][1]['outcomes'][0]['price']['handicap']
                except KeyError: overunder = None
                oddstring = "{0} {2} vs {1} {3} O/U {4}\n".format(team_1, team_2, spread1, spread2, overunder)
                message = message + oddstring
            except IndexError:
                pass

    return message

def bigSpreadWatch(spread_dic):
    source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl").json()
    matchups = source[0]['events']
    text = ''
    for matchup in matchups:
        new_dic, difference = matchupSearch(matchup, spread_dic)
        if difference == True:
            try:
                os.remove('dicfile.txt')
            except FileNotFoundError:
                pass
            old_dic = dicFileRead()
            with open('dicfile.txt', 'w+') as f:
                f.write(str(spread_dic))
            value = { k : new_dic[k] for k in set(new_dic) - set(old_dic) }
            text = text + spreadAlert(value)
    return text

def matchupSearch(matchup, spread_dic):
    difference = False
    id = matchup['id']
    markets = matchup['displayGroups'][0]['markets']
    for market in markets:
        if market['description'] == 'Point Spread':
            pspread = float(market['outcomes'][0]['price']['handicap'])
            check = dicCheck(spread_dic, id)
            if abs(pspread) >= 17.0 and check == False:
                team = market['outcomes'][0]['description']
                string = 'matchup' + str(len(spread_dic)+1)
                spread_dic[string] = {'id':id, 'pspread':pspread, 'team':team}
                difference = True
    return spread_dic, difference

def dicCheck(dic, id):
    for matchup in dic:
        if id == dic[matchup]['id']:
            return True
    return False

def spreadAlert(alert):
    text = ''
    key_list = list(alert.keys())
    for key in key_list:
        spread = str(alert[key]['pspread'])
        text = text + alert[key]['team'] + " " + spread + "\n"
    return text

def dicFileRead():
    try:
        with open('dicfile.txt', 'r') as f:
            dicstring = f.read()
        dicstring = dicstring.replace("\'", "\"")
        spread_dic = json.loads(dicstring)
    except FileNotFoundError:
        spread_dic = {}
    return spread_dic
