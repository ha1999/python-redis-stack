from pprint import pprint
from redis_om import Migrator

from repository import person
from dataloader import loadUserData

# loadUserData()
# Migrator().run()


# pprint(person.findById("01H4A28TRDPKM5MXMN49ESPZ9F"))

# for person in person.findByName("Robert", "McDonald"):
#     pprint(person.dict())
#     print("\n\n\n")

# for person in person.findInRangeAge(30, 47):
#     pprint(person.dict())
#     print("\n\n\n")


# for person in person.findByCityAndSkill("Sheffield", "guitar"):
#     pprint(person.dict())
#     print("\n\n\n")

# for person in person.findByFullTextSearch("play"):
#     pprint(person.dict())
#     print("\n\n\n")


# print(person.updateAgeById("01H4A28TRJ9CV8EMAZVRTJG7JC", 69))

# print(person.deleteById("01H4A28TRGVRND7BEZ6HAPT2PG"))

print(person.setExpirePersonById("01H4A28TRE1MCYXAVSP4XRJAEJ", 10))



