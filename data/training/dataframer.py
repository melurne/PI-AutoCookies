import pickle
import pandas as pd

with open("dataset.pickle", "rb") as f:
    pickled = pickle.load(f)

#print(len(pickled["Others"][0][0][0].tolist() +pickled["Others"][0][0][1].tolist() +pickled["Others"][0][0][2].tolist()))

dataraw = []

for label, liste in pickled.items() :
    for t in liste :
        dataraw.append([])
        print(t.size())
        for word in t[0].tolist() :
            for token in word :
                dataraw[-1].append(token)
        dataraw[-1].append(label)

print(len(dataraw))
