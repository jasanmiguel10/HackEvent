import urllib.request
import json
from hatebase import HatebaseAPI
from pprint import pprint
from PyDictionary import PyDictionary
from profanity import profanity
dictionary=PyDictionary()
Api = "http://api.urbandictionary.com/v0/define?term="
hatebase = HatebaseAPI({"key": 'a4cabaf8fc82b440ffe8cd7fd10c6d70'})
filters = {}
output = "json"
query_type = "sightings"
response = hatebase.performRequest(filters, output, query_type)
lol = json.loads(response)
i = 0
lista = []
while i<100:
    lol = json.loads(response)['data']['datapoint'][i]
    str1 = str(lol)
    if(len((str1.split(","))) == 30 or len((str1.split(","))) == 33):
        lista.append(((str1.split(",")[9]).split(":")[1]))
    else:
        lista.append(((str1.split(",")[8]).split(":")[1]))
    i = i+1
while True:
    twuit = input("Twit")
    boo = False
    for palabras in twuit:
       for words in lista:
            if(palabras == words ):
                boo = True
                break
            break
    if(boo == True or profanity.contains_profanity("twuit") == True):
        print(1)
    else:
       print(0)
