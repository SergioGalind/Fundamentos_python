#Diccionarios
#{"key": "value". }

team ={
    "name": "City",
    "country": "England",
    "champions": 1,
    "players": ['halland', 'grealinsh']
}

print(type(team))
print(team)
print(team["name"])
print(team["players"])
team["players"].append("Kevin")
team["name"]="Manchester City"
team["leage"]="Premier league"
print(team)
