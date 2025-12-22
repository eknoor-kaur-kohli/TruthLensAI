# vertex_integration_example.py
# Example usage only — install google-cloud-aiplatform and set GOOGLE_APPLICATION_CREDENTIALS.
from google.cloud import aiplatform
import os

def vertex_embed(text):
    aiplatform.init(project=os.getenv("GCP_PROJECT"), location="asia-south1")
    embedding_model = aiplatform.TextEmbeddingModel.from_pretrained("textembedding-gecko")
    emb = embedding_model.get_embeddings([text])[0].values
    return emb

def vertex_rag_query(claim, docs_snippets):
    aiplatform.init(project=os.getenv("GCP_PROJECT"), location="asia-south1")
    model = aiplatform.TextGenerationModel.from_pretrained("text-bison@001")
    prompt = f"""You are an evidence-based assistant.
Claim: {claim}
Context snippets:
"""
    for i, s in enumerate(docs_snippets):
        prompt += f"{i+1}) {s['excerpt']} (source: {s['url']})\n"
    prompt += "\nAnswer in JSON: {{'verdict': ..., 'evidence':[...], 'bullets': [...], 'micro_lesson': '...'}}"
    response = model.predict(prompt, max_output_tokens=256, temperature=0.2)
    return response.text
