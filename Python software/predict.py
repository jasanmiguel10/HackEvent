# -*- coding: utf-8 -*-
import pandas as pd
import sys
import re
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from unidecode import unidecode
import numpy as np
tweets = pd.read_excel(sys.argv[1])

print("Column headings:")
print(tweets.columns)

twts  = tweets['content']
lat  = tweets['lat']
long  = tweets['long']
twts_clean = [] 
MAX_NB_WORDS = 20000
#_pattern = re.compile("["
#        u"\U0001F600-\U0001F64F"  # emoticons
#        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#        u"\U0001F680-\U0001F6FF"  # transport & map symbols
#        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                           "]+", flags=re.UNICODE)

for item in twts:
	txt = item.strip()
#	txt = _pattern.sub(r'',txt)
	txt  = re.sub("&.*?;","",txt)
	txt  = re.sub("http.*?\s","",txt)	
#	txt  = re.sub("@.*?\s","",txt)
	twts_clean.append(txt)
twts_clean = [x.encode('utf-8') for x in twts_clean]
tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(twts_clean)
sequences = tokenizer.texts_to_sequences(twts_clean)
query = pad_sequences(sequences, maxlen=1000)
model_ = load_model(sys.argv[2]) 
predicted_labels = []
print type(query)
prediction = model_.predict(query)
print len(prediction.tolist())
for item in prediction:
	 predicted_labels.append(np.argmax(item))

import itertools
import codecs 
with codecs.open('cebo_final.tsv','w') as out:
	for a, b, c in itertools.izip(predicted_labels, lat, long):
		txt = str(a) +'\t' + str(b) + '\t' + str(c) + '\n'
		out.write(txt)	
