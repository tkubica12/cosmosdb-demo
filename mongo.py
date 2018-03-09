import pymongo
import pprint

uri = "mongodb://cosmos-mongodb:iGDmpXn6Usmcj3rlGCn2llEW6rTcHCW8FH9mjyq7ye0tAvy6zoBFsobafqOG6Tz59ewvtr2TsiWlGhlWLwmxfA==@cosmos-mongodb.documents.azure.com:10255/testdb?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)
db = client.mojedb
restaurace = db.restaurace


def singleInsert():
    document = {"name": "Tomas",
        "age": 25,
        "skills": ["math", "singing"],
        "pets": [
            {"type": "dog", "name": "Alik"},
            {"type": "cat", "name": "Micka"}
        ]}
    col1.insert_one(document)
    return

def multiInsert():
    documents = [
        {"name": "Tomas",
            "age": 25,
            "skills": ["math", "singing"],
            "pets": [
                {"type": "dog", "name": "Alik"},
                {"type": "cat", "name": "Micka"}
            ]},
        {"name": "Martin",
            "age": 33,
            "skills": ["math", "cars"],
            "pets": [
                {"type": "dog", "name": "Alik"},
                {"type": "dog", "name": "Tapka"}
            ]},
        {"name": "Lenka",
            "age": 21,
            "skills": ["singing"],
            "pets": []},
        {"name": "Vlasta",
            "age": 46,
            "skills": ["cards", "flowers"],
            "pets": [
                {"type": "cat", "name": "Cicina"},
                {"type": "cat", "name": "Beruska"},
                {"type": "cat", "name": "Linda"},
            ]},
        {"name": "Karel",
            "age": 43,
            "skills": ["painting", "piano"],
            "pets": [
                {"type": "dog", "name": "Alik"},
                {"type": "hamster", "name": "Ferda"}
            ]}]
    col1.insert_many(documents)
    return

def findName(name):
    for doc in col1.find({"name": name}):
        pprint.pprint(doc)
    return

def whoOwns(petname):
    pipeline = [
        {"$match": {"pets.name": petname}},
        {"$project": {"_id":0, "name":1}}
        ]
    for doc in col1.aggregate(pipeline):
        pprint.pprint(doc)
    return

def averageOwnerAge():
    pipeline = [
        {"$match": {"pets": {"$exists":1}}},
        {"$group": {"_id":None, "averageAge":{"$avg": "$age"}}}
        ]
    for doc in col1.aggregate(pipeline):
        pprint.pprint(doc)
    return

def petPerLine():
    pipeline = [
        {"$unwind": "$pets"}
    ]
    for doc in col1.aggregate(pipeline):
        pprint.pprint(doc)
    return

def countPetsPerOwner():
    pipeline = [
        {"$unwind": "$pets"},
        {"$group": {"_id": "$name", "count":{"$sum":1}}}
        # {"$group": {"_id": "$name", "count": {"$sum":"pets.name"}}}
    ]
    for doc in col1.aggregate(pipeline):
        pprint.pprint(doc)
    return

# singleInsert()
# multiInsert()
# findName(name="Karel")
# whoOwns(petname="Alik")
averageOwnerAge()
# petPerLine()
# countPetsPerOwner()






