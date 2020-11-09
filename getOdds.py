import requests

spread_dic = {}


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
    for matchup in matchups:
        spread_dic = matchupSearch(matchup, spread_dic)
    return spread_dic

def matchupSearch(matchup, spread_dic):
    id = matchup['id']
    markets = matchup['displayGroups'][0]['markets']
    for market in markets:
        if market['description'] == 'Point Spread':
            pspread = abs(float(market['outcomes'][0]['price']['handicap']))
            check = dicCheck(spread_dic, id)
            if pspread >= 1.0 and check == False:
                string = 'matchup' + str(len(spread_dic)+1)
                spread_dic[string] = {'id':id, 'pspread':pspread}
    return spread_dic

def dicCheck(dic, id):
    for matchup in dic:
        if id == dic[matchup]['id']:
            return True
    return False
