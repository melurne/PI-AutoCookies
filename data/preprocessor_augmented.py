from transformers import AutoTokenizer, AutoModel
import torch
import os
import pickle
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

tokens = {}

with open("eda_eda.txt", "r") as f :
    for l in f.readlines() :
        if l.split("\t")[0] not in tokens.keys() :
            tokens[l.split("\t")[0]] = []
        tokens[l.split("\t")[0]].append(model(torch.tensor(tokenizer.convert_tokens_to_ids(tokenizer.tokenize(l.split("\t")[1].replace('\n', '').lower())))[None,:])[0])

print(tokens.keys())
for l in tokens.values() :
    print(len(l))

print(tokens["Others"][0].size())

with open("tokens.pickle", 'wb+') as f:
    pickle.dump(tokens, f, protocol=pickle.HIGHEST_PROTOCOL)