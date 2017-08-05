import urllib.request
import json
from pprint import pprint
Api = "http://api.urbandictionary.com/v0/define?term="
while True:
    slag = input("enter slag word")
    response = urllib.request.urlopen(Api + slag)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    print(json_obj)
