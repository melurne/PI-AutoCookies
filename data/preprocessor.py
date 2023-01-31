from transformers import AutoTokenizer, AutoModel
import torch
import os
import pickle
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

tokens = {}

for file in os.listdir("dataset_raw") :
    tokens[file] = []
    with open("dataset_raw/" + file, 'r') as f:
        for l in f.readlines() :
            if l == '\n' :
                continue
            #print(l.replace('\n', '').lower())
            tokens[file].append(model(torch.tensor(tokenizer.convert_tokens_to_ids(tokenizer.tokenize(l.replace('\n', '').lower())))[None,:])[0])

print(tokens.keys())
for l in tokens.values() :
    print(len(l))

print(tokens["Others"][0].size())

with open("tokens.pickle", 'wb+') as f:
    pickle.dump(tokens, f, protocol=pickle.HIGHEST_PROTOCOL)