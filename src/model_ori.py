from __future__ import print_function

import os
import sys
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
import pandas as pd
from keras import backend as K
K.set_image_dim_ordering('tf')
import re
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk import word_tokenize
import string
import pickle
from keras.layers import Dropout

BASE_DIR = '../'
GLOVE_DIR = BASE_DIR + 'data/glove.6B'

MAX_SEQUENCE_LENGTH = 1000	
MAX_NB_WORDS = 20000

EMBEDDING_DIM = 100
VALIDATION_SPLIT = 0.5

data = '/Users/Teban1503/Documents/aihack/data/Reto-Damappa-Dataset/Hackathon_Dataset/Text Datasets/ori_data/all_data.csv'

training_data = '/Users/Teban1503/Documents/aihack/data/Reto-Damappa-Dataset/Hackathon_Dataset/Text Datasets/ori_data/train.csv'

#Index of words

embeddings_index = {}

f = open(os.path.join(GLOVE_DIR, 'glove.6B.100d.txt'))

for line in f:
    values = line.split()
    #print('values : ', len(values))
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()



#Preprocess and clean data 
# second, prepare text samples and their labels
texts = []  # list of text samples
labels_index = {0:'hate',1:'offensive',2:'neither'}  # dictionary mapping label name to numeric id before
labels_bin = {0:'negative',1:'positive'}
labels = []  # list of label ids
stop  = set(stopwords.words('english'))
augmentinfo = []
augmentlabel = [] 

with open(data) as file:
	for item in file:
		data = item.split('\t')
		label_ = data[1]
		text_  = data[2].strip()
		#extra space
		text_  =text_.lower()
			
		#print('BEFORE TEXT: ', text_)
		space_pattern = '\s+'
		giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
		mention_regex = '@[\w\-]+'
		hashtag_regex = '#[\w\-]+'
		parsed_text = re.sub(space_pattern, ' ', text_)
		parsed_text = re.sub(giant_url_regex, '', parsed_text)
		parsed_text = re.sub(mention_regex, '', parsed_text)
		parsed_text  = re.sub("&.*?;",'',parsed_text)
		parsed_text  = re.sub("(\?)+",'?',parsed_text)
		parsed_text  = re.sub("(\!)+",'!',parsed_text)
		parsed_text  = re.sub("(\.)+",'.',parsed_text)
		parsed_text  = re.sub("(\,)+",'.',parsed_text)
		parsed_text  = re.sub("rt\s:",'',parsed_text)
		parsed_text  = re.sub(hashtag_regex,'',parsed_text)


		parsed_text  = " ".join(parsed_text.split())
		#print('AFTER TEXT: ', parsed_text) 

		#tokens = word_tokenize(parsed_text)
		#print('TOKENS: ', tokens)

		texts.append(parsed_text)

		if int(label_)<2:
			labels.append('0')
		else:
			labels.append('1')
		#texto = [i for i in word_tokenize(text_.lower()) if i not in stop] 
		#for ele in texto:
		#	print('%%%')
        #		print (ele)
		#	print('$$$')
        #		test = wordnet.synsets(ele)
		#	print (test)
		#	print('&&&')
   		#texto = " ".join(str(x) for x in texto)
		#texto = texto.translate(None, string.punctuation).strip() 


# finally, vectorize the text samples
tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

print(texts[0])
print(sequences[0])
print(tokenizer.word_index['woman'])
print(embeddings_index['woman'])

word_index = tokenizer.word_index

data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
labels = to_categorical(np.asarray(labels))


indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
validation_samples = int(VALIDATION_SPLIT * data.shape[0])

x_train = data[:-validation_samples]
y_train = labels[:-validation_samples]
x_val = data[-validation_samples:]
y_val = labels[-validation_samples:]

# prepare embedding matrix
# it is a copy of the embedding index and word_index
num_words = min(MAX_NB_WORDS, len(word_index))
embedding_matrix = np.zeros((len(word_index) + 1, EMBEDDING_DIM))
for word, i in word_index.items():
    if i >= MAX_NB_WORDS:
        continue
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector

print(embedding_matrix[385])

print('------------------')
#print(word_index)
embedding_layer = Embedding(len(word_index) + 1,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)

#Important to save the tokenizer to later read to precit
with open("debug_nabetse_default_tutorial_tokenizer_5.pickle", "wb") as f:
   pickle.dump(tokenizer, f)

print('Training model.')
# train a 1D convnet with global maxpooling
sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)
print('$$$$$', embedded_sequences)
print(embedded_sequences)
x = Conv1D(128, 5, activation='relu')(embedded_sequences)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(35)(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
preds = Dense(len(labels_bin), activation='softmax')(x)
model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])
model.fit(x_train, y_train,
          batch_size=128,
          epochs=10,
          validation_data=(x_val, y_val))

model.save('debug_nabetse_default_tutorial_5.h5')


