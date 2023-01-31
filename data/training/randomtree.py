import torch
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
import random

def sample_dict(dc, samplerate=0.1) :
    dict_maj = {}
    dict_min = {}

    for key in dc.keys() :
        random.shuffle(dc[key])
        dict_min[key] = dc[key][:int(len(dc[key])*samplerate)]
        dict_maj[key] = dc[key][int(len(dc[key])*samplerate):]
    return dict_maj, dict_min

def flatten(dc, padding_length) :
    x = []
    y = []
    for label, liste in dc.items() :
        for t in liste :
            x.append([])
            for word in t[0].tolist() :
                for token in word:
                    x[-1].append(token)
            y.append(label)

    for l in x :
        while len(l) < padding_length :
            l.append(0)
    return x, y

with open("dataset_augmented.pickle", "rb") as f:
    pickled = pickle.load(f)

# Padd les points AVANT de split
x = []
for label, liste in pickled.items() :
    for t in liste :
        x.append([])
        for word in t[0].tolist() :
            for token in word:
                x[-1].append(token)
lenmax = max([len(t) for t in x])


 

trainset, evalset = sample_dict(pickled, samplerate=0.2)

x_train, y_train = flatten(trainset, lenmax) 
x_eval, y_eval = flatten(evalset, lenmax) 

#print([len(t) for t in x_train])

model = RandomForestClassifier()
model.fit(x_train, y_train)
print(model.score(x_eval, y_eval))

print(classification_report(y_eval, model.predict(x_eval), output_dict = True))

with open("report_augmented.pickle", "wb+") as f:
    pickle.dump(classification_report(y_eval, model.predict(x_eval), output_dict = True), f)

