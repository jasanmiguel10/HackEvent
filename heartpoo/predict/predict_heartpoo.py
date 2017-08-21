# -*- coding: utf-8 -*-
import pandas as pd
import sys
import re
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import text_to_word_sequence

from keras.layers import Embedding
from unidecode import unidecode
from keras.models import Model
import numpy as np
from keras.layers import Dense, Input, Flatten
import pickle

MAX_NB_WORDS     = 20000
tokenizer_pickle = 'HackEvent/heartpoo/model/default_tutorial_tokenizer_5.pickle'
model_cnn        = 'HackEvent/heartpoo/model/default_tutorial_5.h5'

txt = sys.argv[1]
print('%%%')
print(len(txt))
txt = txt.strip()
txt_sq = [txt]

#Still needs to get clean pre-process data 
#txt = _pattern.sub(r'',txt)
#txt  = re.sub("&.*?;","",txt)
#txt  = re.sub("http.*?\s","",txt)	
#txt  = re.sub("@.*?\s","",txt)

#Test_data
#input_1 = 'word is you use roids, stupid hypocrite lying faggots.'
#input_2 = 'some species of birds have been known to hold funerals for their deceased.'

with open(tokenizer_pickle, "rb") as f:
   tokenizer = pickle.load(f)

#seq_c = text_to_word_sequence(txt,filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',lower=True,split=" ")
#test = sequence_to_matrix(seq_c)
sequences = tokenizer.texts_to_sequences(txt_sq)

query = pad_sequences(sequences, maxlen=1000)
model_ = load_model(model_cnn) 
predicted_labels = []

prediction = model_.predict(query)
print (prediction)
for item in prediction:
	 predicted_labels.append(np.argmax(item))

print predicted_labels
