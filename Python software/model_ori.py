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

BASE_DIR = ''
GLOVE_DIR = BASE_DIR + 'data/glove.6B'
MAX_SEQUENCE_LENGTH = 1000
MAX_NB_WORDS = 20000
EMBEDDING_DIM = 100
VALIDATION_SPLIT = 0.2

data = '/Users/Teban1503/Documents/aihack/data/Reto-Damappa-Dataset/Hackathon_Dataset/Text Datasets/ori_data/all_data.csv'
training_data = '/Users/Teban1503/Documents/aihack/data/Reto-Damappa-Dataset/Hackathon_Dataset/Text Datasets/ori_data/train.csv'
# first, build index mapping words in the embeddings set
# to their embedding vector

print('Indexing word vectors.')

embeddings_index = {}
f = open(os.path.join(GLOVE_DIR, 'glove.6B.100d.txt'))
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))


#Preprocess and clean data 


# second, prepare text samples and their labels
print('Processing text dataset')

texts = []  # list of text samples
labels_index = {0:'hate',1:'offensive',2:'neither'}  # dictionary mapping label name to numeric id
labels = []  # list of label ids
stop  = set(stopwords.words('english'))
augmentinfo = []
augmentlabel = [] 
with open(data) as file:
	for item in file:
		data = item.split('\t')
		label_ = data[1]
		text_  = data[2].strip()
		text_  = re.sub("&.*?;","",text_)
		text_  = re.sub("http.*?\s","",text_)
		text_  = re.sub("@.*?\s","",text_)
		texto = [i for i in word_tokenize(text_.lower()) if i not in stop] 
		for ele in texto:
			print('%%%')
        		print (ele)
			print('$$$')
        		test = wordnet.synsets(ele)
			print (test)
			print('&&&')
   		texto = " ".join(str(x) for x in texto)
		texto = texto.translate(None, string.punctuation).strip()
   		texts.append(texto)
		#print (texto)
		labels.append(label_)

print('Found %s texts.' % len(texts))


# finally, vectorize the text samples into a 2D integer tensor
tokenizer = Tokenizer(num_words=MAX_NB_WORDS)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

word_index = tokenizer.word_index
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
'''
labels = to_categorical(np.asarray(labels))
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

# split the data into a training set and a validation set
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
num_validation_samples = int(VALIDATION_SPLIT * data.shape[0])

x_train = data[:-num_validation_samples]
y_train = labels[:-num_validation_samples]
x_val = data[-num_validation_samples:]
y_val = labels[-num_validation_samples:]

print('Preparing embedding matrix.')

# prepare embedding matrix
num_words = min(MAX_NB_WORDS, len(word_index))
embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))

for word, i in word_index.items():
    if i >= MAX_NB_WORDS:
        continue
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector

# load pre-trained word embeddings into an Embedding layer
# note that we set trainable = False so as to keep the embeddings fixed
embedding_layer = Embedding(num_words,
                            EMBEDDING_DIM,
                            weights=[embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)

print('Training model.')

# train a 1D convnet with global maxpooling
sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)
x = Conv1D(128, 5, activation='relu')(embedded_sequences)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(5)(x)
x = Conv1D(128, 5, activation='relu')(x)
x = MaxPooling1D(35)(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
preds = Dense(len(labels_index), activation='softmax')(x)

model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])

model.fit(x_train, y_train,
          batch_size=128,
          epochs=10,
          validation_data=(x_val, y_val))

model.save('model.20.2.h5')
'''
