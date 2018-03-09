# Import dat
mongoimport --db mojedb \
            --collection zviratka \
            --file ./zviratka.json \
            --jsonArray \
            --host mojesupercosmos.documents.azure.com \
            --username mojesupercosmos \
            --password "cy7gdeXjALjF33tgxGyQcMC5E1oSxAEPggSLJHHG8iByYM7uKNzCATWAe8kjUZcgQCxQvNJJ8KPFcGYtFlNpew==" \
            --port 10255 \
            --ssl \
            --sslAllowInvalidCertificates




# Search

{"zviratko" : "pes"}
{"klasifikace.trida" : "savci"}
{"prumerne_doziti": {$gt: 10}}
{"hodnoceni.jmeno" : "Tomas"}


# Python

pip install pymongo
python
import pymongo
uri = "mongodb://mojesupercosmos:cy7gdeXjALjF33tgxGyQcMC5E1oSxAEPggSLJHHG8iByYM7uKNzCATWAe8kjUZcgQCxQvNJJ8KPFcGYtFlNpew==@mojesupercosmos.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)
db = client.mojedb
zviratka = db.zviratka
for doc in zviratka.find({"klasifikace.trida" : "savci"}):
    print doc


$ pip install pymongo
$ python
Python 2.7.12 (default, Nov 19 2016, 06:48:10)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pymongo
>>> uri = "mongodb://mojesupercosmos:cy7gdeXjALjF33tgxGyQcMC5E1oSxAEPggSLJHHG8iByYM7uKNzCATWAe8kjUZcgQCxQvNJJ8KPFcGYtFlNpew==@mojesupercosmos.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
>>> client = pymongo.MongoClient(uri)
nt.>>> db = client.mojedb
>>> zviratka = db.zviratka
>>> for doc in zviratka.find({"klasifikace.trida" : "savci"}):
...     print doc
...
{u'zviratko': u'pes', u'_id': ObjectId('5a97c1a8466f0d201065f880'), u'hodnoceni': [{u'hvezdicky': 5.0, u'jmeno': u'Anicka'}, {u'hvezdicky': 3.0, u'jmeno': u'Tomas'}, {u'hvezdicky': 4.0, u'jmeno': u'Marek'}], u'klasifikace': {u'rad': u'selmy', u'trida': u'savci'}, u'prumerne_doziti': 12.0}
{u'zviratko': u'kocka', u'_id': ObjectId('5a97c1a8466f0d201065f881'), u'hodnoceni': [{u'hvezdicky': 4.0, u'jmeno': u'Anicka'}, {u'hvezdicky': 4.0, u'jmeno': u'Karel'}, {u'hvezdicky': 2.0, u'jmeno': u'Martin'}], u'klasifikace': {u'rad': u'selmy', u'trida': u'savci'}, u'prumerne_doziti': 10.0}
{u'zviratko': u'krecek', u'_id': ObjectId('5a97c1a8466f0d201065f882'), u'hodnoceni': [{u'hvezdicky': 4.0, u'jmeno': u'Anicka'}], u'klasifikace': {u'rad': u'hlodavci', u'trida': u'savci'}, u'prumerne_doziti': 2.0}
{u'zviratko': u'morce', u'_id': ObjectId('5a97c1a8466f0d201065f883'), u'hodnoceni': [{u'hvezdicky': 3.0, u'jmeno': u'Petr'}, {u'hvezdicky': 4.0, u'jmeno': u'Tomas'}], u'klasifikace': {u'rad': u'hlodavci', u'trida': u'savci'}, u'prumerne_doziti': 4.0}

{u'zviratko': u'pes', u'_id': ObjectId('5a9708ca0e0d6d2a5c6786a2'), u'hodnoceni': [{u'hvezdicky': 5, u'jmeno': u'Anicka'}, {u'hvezdicky': 3, u'jmeno': u'Tomas'}, {u'hvezdicky': 4, u'jmeno': u'Marek'}], u'klasifikace': {u'rad': u'selmy', u'trida': u'savci'}, u'prumerne_doziti': 12}
{u'zviratko': u'kocka', u'_id': ObjectId('5a9708ca0e0d6d2a5c6786a3'), u'hodnoceni': [{u'hvezdicky': 4, u'jmeno': u'Anicka'}, {u'hvezdicky': 4, u'jmeno': u'Karel'}, {u'hvezdicky': 2, u'jmeno': u'Martin'}], u'klasifikace': {u'rad': u'selmy', u'trida': u'savci'}, u'prumerne_doziti': 10}
{u'zviratko': u'krecek', u'_id': ObjectId('5a9708ca0e0d6d2a5c6786a4'), u'hodnoceni': [{u'hvezdicky': 4, u'jmeno': u'Anicka'}], u'klasifikace': {u'rad': u'hlodavci', u'trida': u'savci'}, u'prumerne_doziti': 2}
{u'zviratko': u'morce', u'_id': ObjectId('5a9708ca0e0d6d2a5c6786a5'), u'hodnoceni': [{u'hvezdicky': 3, u'jmeno': u'Petr'}, {u'hvezdicky': 4, u'jmeno': u'Tomas'}], u'klasifikace': {u'rad': u'hlodavci', u'trida': u'savci'}, u'prumerne_doziti': 4}
>>>

# Mongo shell

mongo mojesupercosmos.documents.azure.com:10255 -u mojesupercosmos -p cy7gdeXjALjF33tgxGyQcMC5E1oSxAEPggSLJHHG8iByYM7uKNzCATWAe8kjUZcgQCxQvNJJ8KPFcGYtFlNpew== --ssl --sslAllowInvalidCertificates

globaldb:PRIMARY> use mojedb
switched to db mojedb

# Find zviratka, ktere hodnotil Tomas
globaldb:PRIMARY> db.zviratka.find({"hodnoceni.jmeno" : "Tomas"})
{ "_id" : ObjectId("5a9708ca0e0d6d2a5c6786a2"), "zviratko" : "pes", "klasifikace" : { "trida" : "savci", "rad" : "selmy" }, "prumerne_doziti" : 12, "hodnoceni" : [ { "jmeno" : "Anicka", "hvezdicky" : 5 }, { "jmeno" : "Tomas", "hvezdicky" : 3 }, { "jmeno" : "Marek", "hvezdicky" : 4 } ] }
{ "_id" : ObjectId("5a9708ca0e0d6d2a5c6786a5"), "zviratko" : "morce", "klasifikace" : { "trida" : "savci", "rad" : "hlodavci" }, "prumerne_doziti" : 4, "hodnoceni" : [ { "jmeno" : "Petr", "hvezdicky" : 3 }, { "jmeno" : "Tomas", "hvezdicky" : 4 } ] }
{ "_id" : ObjectId("5a9708ca0e0d6d2a5c6786a7"), "zviratko" : "andulka", "klasifikace" : { "trida" : "ptaci", "rad" : "papousci" }, "prumerne_doziti" : 10, "hodnoceni" : [ { "jmeno" : "Lenka", "hvezdicky" : 2 }, { "jmeno" : "Tomas", "hvezdicky" : 4 }, { "jmeno" : "Petra", "hvezdicky" : 3 } ] }
{ "_id" : ObjectId("5a9708ca0e0d6d2a5c6786a8"), "zviratko" : "zelva", "klasifikace" : { "trida" : "plazy", "rad" : "zelvy" }, "prumerne_doziti" : 100, "hodnoceni" : [ { "jmeno" : "Lenka", "hvezdicky" : 5 }, { "jmeno" : "Tomas", "hvezdicky" : 4 }, { "jmeno" : "Karel", "hvezdicky" : 5 }, { "jmeno" : "Petra", "hvezdicky" : 4 } ] }

# Vypsat jen zviratka a klasifikaci
db.zviratka.find({},{"zviratko": 1, "klasifikace.trida": 1, "_id": 0})
{ "zviratko" : "pes", "klasifikace" : { "trida" : "savci" } }
{ "zviratko" : "kocka", "klasifikace" : { "trida" : "savci" } }
{ "zviratko" : "krecek", "klasifikace" : { "trida" : "savci" } }
{ "zviratko" : "morce", "klasifikace" : { "trida" : "savci" } }
{ "zviratko" : "kakadu", "klasifikace" : { "trida" : "ptaci" } }
{ "zviratko" : "andulka", "klasifikace" : { "trida" : "ptaci" } }
{ "zviratko" : "zelva", "klasifikace" : { "trida" : "plazy" } }

# Update, pridani do array

db.zviratka.update(
    { "zviratko": "pes" },
    { $push: 
        { 
            "hodnoceni": {
                "jmeno": "Tina",
                "hvezdicky": 5
            }
        } 
    }
)

db.zviratka.find({"hodnoceni.jmeno" : "Tina"})


globaldb:PRIMARY> db.zviratka.update(
...     { "zviratko": "pes" },
...     { $push:
...         {
...             "hodnoceni": {
...                 "jmeno": "Tina",
...                 "hvezdicky": 5
...             }
...         }
...     }
... )
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
globaldb:PRIMARY> db.zviratka.find({"hodnoceni.jmeno" : "Tina"})
{ "_id" : ObjectId("5a9708ca0e0d6d2a5c6786a2"), "zviratko" : "pes", "klasifikace" : { "trida" : "savci", "rad" : "selmy" }, "prumerne_doziti" : 12, "hodnoceni" : [ { "jmeno" : "Anicka", "hvezdicky" : 5 }, { "jmeno" : "Tomas", "hvezdicky" : 3 }, { "jmeno" : "Marek", "hvezdicky" : 4 }, { "jmeno" : "Tina", "hvezdicky" : 5 } ] }

# Check RUs
db.runCommand({getLastRequestStatistics: 1})

globaldb:PRIMARY> db.runCommand({getLastRequestStatistics: 1})
{
        "_t" : "GetRequestStatisticsResponse",
        "ok" : 1,
        "CommandName" : "OP_QUERY",
        "RequestCharge" : 6.21,
        "RequestDurationInMilliSeconds" : NumberLong(3)
}

# Agregace

## Koho hodnotil Tomas
db.zviratka.aggregate([
    { $match: { "hodnoceni.jmeno": "Tomas" }}
    { $project: { zviratko: 1, hodnoceni: 1 }},
    { $unwind: {
        path: "$hodnoceni"
    } },
])

db.runCommand({getLastRequestStatistics: 1})

## Kolik zvirat

db.zviratka.aggregate([
    { $group: { _id: null, celkem: { $sum: 1 } } }
])

globaldb:PRIMARY> db.zviratka.aggregate([                        
...     { $group: { _id: null, celkem: { $sum: 1 } } }     
... ])                                                           
{                                                                
        "_t" : "AggregationPipelineResponse",                    
        "ok" : 1,                                                
        "waitedMS" : NumberLong(0),                              
        "result" : [                                             
                {                                                
                        "_id" : "zviratko",                      
                        "celkem" : 7                             
                }                                                
        ]                                                        
}                                                                

## Kolik savcu

db.zviratka.aggregate([
    { $match : { "klasifikace.trida": "savci" }},
    { $group: { _id: null, celkem: { $sum: 1 } } }
])

globaldb:PRIMARY> db.zviratka.aggregate([
...     { $match : { "klasifikace.trida": "savci" }},
...     { $group: { _id: null, celkem: { $sum: 1 } } }
... ])
{
        "_t" : "AggregationPipelineResponse",
        "ok" : 1,
        "waitedMS" : NumberLong(0),
        "result" : [
                {
                        "_id" : "zviratko",
                        "celkem" : 4
                }
        ]
}
globaldb:PRIMARY> db.runCommand({getLastRequestStatistics: 1})
{
        "_t" : "GetRequestStatisticsResponse",
        "ok" : 1,
        "CommandName" : "aggregate",
        "RequestCharge" : 5.06,
        "RequestDurationInMilliSeconds" : NumberLong(15)
}

## Pocty ve tridach a seradit

db.zviratka.aggregate([
    { $group: { _id: "$klasifikace.trida", celkem: { $sum: 1 } } },
    { $sort: { celkem: -1 } }
])


globaldb:PRIMARY> db.zviratka.aggregate([
...     { $group: { _id: "$klasifikace.trida", celkem: { $sum: 1 } } },
...     { $sort: { celkem: -1 } }
... ])
{
        "_t" : "AggregationPipelineResponse",
        "ok" : 1,
        "waitedMS" : NumberLong(0),
        "result" : [
                {
                        "_id" : "savci",
                        "celkem" : 4
                },
                {
                        "_id" : "ptaci",
                        "celkem" : 2
                },
                {
                        "_id" : "plazy",
                        "celkem" : 1
                }
        ]
}
globaldb:PRIMARY> db.runCommand({getLastRequestStatistics: 1})
{
        "_t" : "GetRequestStatisticsResponse",
        "ok" : 1,
        "CommandName" : "aggregate",
        "RequestCharge" : 4.44,
        "RequestDurationInMilliSeconds" : NumberLong(14)
}

# Delka zivota podle tridy

db.zviratka.aggregate([
    { $group: { _id: "$klasifikace.trida", delka_zivota: { $avg: "$prumerne_doziti" } } },
    { $sort: { delka_zivota: -1 } }
])



globaldb:PRIMARY> db.zviratka.aggregate([
...     { $group: { _id: "$klasifikace.trida", delka_zivota: { $avg: "$prumerne_doziti" } } },
rt..    { $sort: { celkem: -1 } }
... ])
{
        "_t" : "AggregationPipelineResponse",
        "ok" : 1,
        "waitedMS" : NumberLong(0),
        "result" : [
                {
                        "_id" : "savci",
                        "delka_zivota" : NumberLong(7)
                },
                {
                        "_id" : "ptaci",
                        "delka_zivota" : NumberLong(20)
                },
                {
                        "_id" : "plazy",
                        "delka_zivota" : NumberLong(100)
                }
        ]
}

# Prumerne hodnoceni

db.zviratka.aggregate([
    { $project: { zviratko: 1, hodnoceni: 1 }},
    { $unwind: {
        path: "$hodnoceni"
    } },
    { $group: { _id: "$zviratko", delka_zivota: { $avg: "$hodnoceni.hvezdicky" } } },
])

db.runCommand({getLastRequestStatistics: 1})

db.zviratka.aggregate([
    { $project: { zviratko: 1, hodnoceni: 1 }},
    { $unwind: {
        path: "$hodnoceni"
    } },
    { $group: { _id: "$zviratko", NumberDecimal(delka_zivota): { $avg: "$hodnoceni.hvezdicky" } } },
])
