from transformers import AutoTokenizer, AutoModel
import torch
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
print(tokenizer.tokenize("return maximum value"))

tokens = tokenizer.tokenize("apply market research to generate audience insights")
tokens_ids=tokenizer.convert_tokens_to_ids(tokens)
context_embeddings=model(torch.tensor(tokens_ids)[None,:])[0]

print(context_embeddings)