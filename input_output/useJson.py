import json
# JSON ( Javascript Object Notation)

# de JSON → structure de donnée python : sérialisation
# structure de donnée python → json : deserialization

mon_dictionnaire = {
    "a": 12,
    "b": 13,
    "c": 14,
    "d": None
}
mon_dictionnaire_json = json.dumps(mon_dictionnaire)  # permet de mettre un element sous forme de json
mon_dictionnaire_json = json.loads(mon_dictionnaire_json)  # permet de revenir au format de structure de données python

with open("data.json", 'r+') as f:
    json.dump(mon_dictionnaire, f)
    f.seek(0)  # permet de ramener le curseur au debut du fichier
    text = json.load(f)
    print(type(text))
    print(text)