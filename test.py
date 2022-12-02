import sqlite3

data = sqlite3.connect("data/jo.db")
values = {}

request1a = '''
WITH
    uniquePlayerNumbers AS (
        SELECT DISTINCT numSp, pays, nomSp, prenomSp from LesSportifsEQ
    ),
    nbBronze as (
        SELECT pays, COUNT(bronze) as nbBronze from LesResultats
        JOIN uniquePlayerNumbers ON LesResultats.bronze = uniquePlayerNumbers.numSp
        WHERE bronze > 1000
        GROUP BY pays
    )
SELECT * from nbBronze;
'''

request1b = '''
WITH
    uniqueTeamNumbers AS (
        SELECT DISTINCT pays, numEq  from LesSportifsEQ
    ),
    nbBronzeTeam as (
        SELECT pays, COUNT(bronze) as nbBronze from LesResultats
        JOIN uniqueTeamNumbers ON LesResultats.bronze = uniqueTeamNumbers.numEq
        GROUP BY pays
    )
SELECT * FROM nbBronzeTeam; 
'''

request2a = '''
WITH
    uniquePlayerNumbers AS (
        SELECT DISTINCT numSp, pays, nomSp, prenomSp from LesSportifsEQ
    ),
    nbSilver as (
        SELECT pays, COUNT(silver) as nbArgent from LesResultats
        JOIN uniquePlayerNumbers ON LesResultats.silver = uniquePlayerNumbers.numSp
        WHERE silver > 1000
        GROUP BY pays
    )
SELECT * from nbSilver;
'''

request2b = '''
WITH
    uniqueTeamNumbers AS (
        SELECT DISTINCT pays, numEq  from LesSportifsEQ
    ),
    nbSilverTeam as (
        SELECT pays, COUNT(silver) as nbArgent from LesResultats
        JOIN uniqueTeamNumbers ON LesResultats.silver = uniqueTeamNumbers.numEq
        GROUP BY pays
    )
SELECT * FROM nbSilverTeam;
'''

request3a = '''
WITH
    uniquePlayerNumbers AS (
        SELECT DISTINCT numSp, pays, nomSp, prenomSp from LesSportifsEQ
    ),
    nbGold as (
        SELECT pays, COUNT(gold) as nbOr from LesResultats
        JOIN uniquePlayerNumbers ON LesResultats.gold = uniquePlayerNumbers.numSp
        WHERE gold > 1000
        GROUP BY pays
    )
SELECT * from nbGold;
'''

request3b = '''
WITH
    uniqueTeamNumbers AS (
        SELECT DISTINCT pays, numEq  from LesSportifsEQ
    ),
    nbGoldTeam as (
        SELECT pays, COUNT(gold) as nbOr from LesResultats
        JOIN uniqueTeamNumbers ON LesResultats.gold = uniqueTeamNumbers.numEq
        GROUP BY pays
    )
SELECT * FROM nbGoldTeam;
'''

# Bronze


def getMedals(request, medalType, isTeam = False):
    if isTeam:
        getTeamMedals(request, medalType)
        return

    for row in data.cursor().execute(request):
        if row[0] in values:
            values[row[0]][medalType] = row[1]
        else:
            values[row[0]] = {medalType: row[1]}


def getTeamMedals(request, medalType):
    for row in data.cursor().execute(request):
        if row[0] in values and medalType in values[row[0]]:
            values[row[0]][medalType] = values[row[0]][medalType] + row[1]
        elif not row[0] in values:
            values[row[0]] = {medalType: row[1]}
        else:
            values[row[0]][medalType] = row[1]


getMedals(request1a, "bronze")
# getMedals(request1a, "bronze", isTeam=True)

print(values)
# dict["france"] = {"gold": 1, "silver": 2, "bronze": 3}