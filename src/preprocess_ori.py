import pandas as pd
import sys
import numpy as np
from sklearn.model_selection import train_test_split
#Reads columns from csv file
tweets = pd.read_csv(sys.argv[1])

tweets.to_csv("all_data.csv", sep='\t',header=None,encoding='utf-8')
#Categories 0,1,2 (0 is hate speech, 1 is offensive and 2 is neither)
#Splits data into 60% training, 20% dev, 20 % test
train, dev, test = np.split(tweets.sample(frac=1), [int(.6*len(tweets)), int(.8*len(tweets))])


#Export new splited data
train_pd    = pd.DataFrame(train)
dev_pd     = pd.DataFrame(dev)
test_pd = pd.DataFrame(test)

train_y = train_pd['class']
train_x = train_pd['tweet']

test_y = test_pd['class']
test_x = test_pd['tweet']

dev_y = test_pd['class']
dev_x = test_pd['tweet']

train_pd.to_csv("train.csv", sep='\t',header=None,encoding='utf-8')
test_pd.to_csv("test.csv", sep='\t',header=None,encoding='utf-8')
dev_pd.to_csv("dev.csv", sep='\t',header=None, encoding='utf-8')

