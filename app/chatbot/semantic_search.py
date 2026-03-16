from sentence_transformers import SentenceTransformer, util
from .intents import INTENTS
import torch

model = SentenceTransformer("all-MiniLM-L6-v2") 

intent_sentences = []
intent_labels = []

for intent, examples in INTENTS.items():
    for sentence in examples:
        intent_sentences.append(sentence)
        intent_labels.append(intent)

intent_embeddings = model.encode(intent_sentences, convert_to_tensor=True)


def semantic_intent(message: str) -> str:

    query_embedding = model.encode(message, convert_to_tensor=True)

    scores = util.cos_sim(query_embedding, intent_embeddings)[0]

    best_idx = torch.argmax(scores)

    return intent_labels[best_idx]