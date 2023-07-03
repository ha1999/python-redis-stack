import json

from repository.person import savePerson

def loadUserData():
    with open('data/people.json', encoding='utf-8') as f:
        people = json.loads(f.read())

    for person in people:
        r = savePerson(person)
        print(f"Created person {person['first_name']} {person['last_name']} with ID {r}")
    