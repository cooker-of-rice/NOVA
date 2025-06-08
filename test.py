import torch
import pickle
import sys
import os

# ✅ Fix: Add nanoGPT directory, not the file itself
sys.path.append(os.path.join(os.getcwd(), "nanoGPT"))

from model import GPT, GPTConfig

# === Load vocab ===
with open("nova_model/meta.pkl", "rb") as f:
    meta = pickle.load(f)

stoi = meta["stoi"]
itos = meta["itos"]
vocab_size = len(stoi)

# === Helpers ===
def encode(text):
    return [stoi.get(c, 0) for c in text]

def decode(tokens):
    return ''.join([itos[i] for i in tokens])

# === Load model checkpoint ===
checkpoint = torch.load("nova_model/ckpt.pt", map_location='cpu')

# Fallback: define model structure manually
model_args = checkpoint.get("model_args", {
    "vocab_size": vocab_size,
    "block_size": 128,
    "n_layer": 4,
    "n_head": 4,
    "n_embd": 128,
    "dropout": 0.1,
})

model = GPT(GPTConfig(**model_args))
model.load_state_dict(checkpoint["model"])
model.eval()

# === Prompt ===
prompt = "User: I'm feeling down\nNOVA:"
input_ids = torch.tensor([encode(prompt)], dtype=torch.long)

# === Generate ===
with torch.no_grad():
    output = model.generate(input_ids, max_new_tokens=100)

# === Output ===
print("\n🧠 NOVA says:")
print(decode(output[0].tolist()))
