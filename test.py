import torch
import pickle
from model import GPT, GPTConfig

# Load metadata (vocab info)
with open("model/meta.pkl", "rb") as f:
    meta = pickle.load(f)

stoi = meta["stoi"]
itos = meta["itos"]

vocab_size = len(stoi)

# Encode/decode helpers
def encode(s):
    return [stoi.get(c, 0) for c in s]

def decode(l):
    return ''.join([itos[i] for i in l])

# Load model checkpoint
checkpoint = torch.load("model/ckpt.pt", map_location='cpu')
model_args = checkpoint['config']['model_args']
model = GPT(GPTConfig(**model_args))
model.load_state_dict(checkpoint['model'])
model.eval()

# Prompt the model
context = "User: I'm stressed\nNOVA:"
input_ids = torch.tensor([encode(context)], dtype=torch.long)

# Generate
with torch.no_grad():
    output = model.generate(input_ids, max_new_tokens=100)

# Print result
print(decode(output[0].tolist()))
