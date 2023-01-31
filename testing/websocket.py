import asyncio
from websockets import serve
from transformers import AutoTokenizer, AutoModel
from sklearn.ensemble import RandomForestClassifier
import torch
import pickle
import json

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
with open("model_RandomForestClassifier.pickle", "rb") as f:
    classifier = pickle.load(f)

padding_length = 9216

def classify(phrase) :
    tokens = tokenizer.tokenize(phrase.lower())
    tokens_ids=tokenizer.convert_tokens_to_ids(tokens)
    context_embeddings=model(torch.tensor(tokens_ids)[None,:])[0]
    x = []
    for word in context_embeddings[0].tolist() :
        for token in word:
            x.append(token)
    while len(x) < padding_length :
        x.append(0)
    return classifier.predict([x])[0].replace(".txt", "")


async def echo(websocket):
    async for message in websocket:
        m = json.loads(message)
        print(m)
        response = json.dumps({"id": m["id"], "category": classify(m["text"])})
        await websocket.send(response)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())

