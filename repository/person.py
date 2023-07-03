from models.persion import Person


def savePerson(json_person):
    new_persion = Person(**json_person)
    new_persion.save()
    return new_persion.pk


def findById(person_id: str):
    person = Person.get(person_id)
    return person.dict()


def findByName(first_name: str, last_name: str):
    return Person.find(
        (Person.first_name == first_name) & (Person.last_name == last_name)
    ).all()


def findInRangeAge(min_age: int, max_age: int):
    return (
        Person.find((Person.age >= min_age) & (Person.age <= max_age))
        .sort_by("age")
        .all()
    )


def findByCityAndSkill(city: str, skill: str):
    return Person.find((Person.skills << skill) & (Person.address.city == city)).all()


def findByFullTextSearch(text_search: str):
    return Person.find(Person.personal_statement % text_search).all()

def updateAgeById(person_id: str, age: int):
    person = Person.get(person_id)
    person.age = age
    person.save()
    return person.dict()

def deleteById(person_id: str):
    return Person.delete(person_id)

def setExpirePersonById(person_id: str, ttl: int):
    person_to_expire = Person.get(person_id)
    return Person.db().expire(person_to_expire.key(), ttl)
