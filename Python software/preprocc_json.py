import json
from pprint import pprint
import sys 
import codecs

data = []
with codecs.open(sys.argv[1],'rU','utf-8') as archivo :
	for line in archivo:
			data.append(json.loads(line))

pprint(data)
