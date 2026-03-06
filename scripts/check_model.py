
from sentence_transformers import SentenceTransformer
import time

try:
    print("Loading model...")
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    print("Model loaded.")
    emb = model.encode(["test"])
    print(f"Embedding generated: {emb.shape}")
except Exception as e:
    print(f"Error: {e}")
