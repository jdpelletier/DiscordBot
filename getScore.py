from urllib.request import urlopen
import re

#test for reading scores

logo_dict = {"ari.png" : "Arizona",
             "atl.png" : "Atlanta",
             "car.png" : "Carolina",
             "chi.png" : "Chicago",
             "dal.png" : "Dallas",
             "det.png" : "Detroit",
             "gb.png" : "Green Bay",
             "lar.png" : "LA Rams",
             "min.png" : "Minnesota",
             "no.png" : "New Orleans",
             "nyg.png" : "New York Giants",
             "phi.png" : "Philadelphia",
             "sf.png" : "San Fransisco",
             "sea.png" : "Seattle",
             "tb.png" : "Tampa Bay",
             "wsh.png" : "Washington",
             "bal.png" : "Baltimore",
             "buf.png" : "Buffalo",
             "cin.png" : "Cincinnati",
             "cle.png" : "Clevland",
             "den.png" : "Denver",
             "hou.png" : "Houston",
             "ind.png" : "Indianapolis",
             "jax.png" : "Jacksonville",
             "kc.png" : "Kansas City",
             "lv.png" : "Las Vegas",
             "lac.png" : "LA Chargers",
             "mia.png" : "Miami",
             "ne.png" : "New England",
             "nyj.png" : "New York Jets",
             "pit.png" : "Pittsburg",
             "ten.png" : "Tennesse"
            }

# def getTeam(team):
#     team_dict = {'houston' : 'hou.png',
#                  'kansascity' : 'kc.png'
#                  }
#     return team_dict[team]
#
# def formatTeam(team):
#     name_dict = {'houston' : 'Houston',
#                  'kansascity' : 'Kansas City'
#                  }
#     return name_dict[team]

def findLogos(html):
    matches = re.finditer("png", html)
    matches_positions = [match.start() for match in matches]
    return matches_positions

def allScores():
    url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    matches_positions = findLogos(html)
    teamlist = []
    scorelist = []
    for match in matches_positions:
        if html[match-4] == '/':
            team = html[match-3:match+3]
        else:
            team = html[match-4:match+3]
        if team in logo_dict:
            team = logo_dict[team]
            teamlist.append(team)
            if html[match+16] == '"':
                score = html[match+15]
            else:
                score = html[match+15:match+17]
            scorelist.append(score)
    message = " This week's scores:\n---------------------------------\n"
    # print(teamlist)
    # print(scorelist)
    for i in range(0,len(teamlist)-1,2):
        team1 = teamlist[i]
        team2 = teamlist[i+1]
        score1 = scorelist[i]
        score2 = scorelist[i+1]
        scorestring = f"\n{team1} {score1} {team2} {score2}"
        message = message + scorestring

    return message

# def getScore(team1, team2):
#     url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=20200910"
#     page = urlopen(url)
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#     logo = getTeam(team1.lower())
#     logostart = html.find(logo)
#     score = logostart + len(logo) + 12
#     score1 = html[score:score+2]
#     logo = getTeam(team2.lower())
#     logostart = html.find(logo)
#     score = logostart + len(logo) + 12
#     score2 = html[score:score+2]
#     team1 = formatTeam(team1)
#     team2 = formatTeam(team2)
#     readout = f"{team1} {score2} {team2} {score2}"
#     return readout
