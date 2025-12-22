import os
import re
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from sample_data import SAMPLE_FACT_CHECKS
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes in your app.

# CONFIG: switch to "vertex" to use Vertex AI integration (see vertex_integration_example.py)
MODE = os.getenv("MODE", "mock") # "mock" or "vertex"
MAX_EVIDENCE = 3

def extract_claim(text):
    """
    Simple claim extractor:
     - picks the first sentence with a verb and more than 5 words.
     This is heuristic; replace with a prompt-based extractor for better results.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    for s in sentences:
        words = s.split()
        if len(words) >= 5 and re.search(r'\b(is|are|was|were|claims|says|causes|cures|does)\b', s, re.I):
            return s.strip()
    # fallback: first sentence of input
    return sentences[0].strip() if sentences else text.strip()

def local_vector_search(claim, top_k=MAX_EVIDENCE):
    """
    Mock vector search: finds fact-checks with overlapping words.
    Replace with Vertex Vector Search index queries for production.
    """
    ck = claim.lower()
    scored = []
    for doc in SAMPLE_FACT_CHECKS:
        score = sum(1 for w in doc["claim"].lower().split() if w in ck)
        if score > 0:
            scored.append((score, doc))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [d for _, d in scored[:top_k]]

def assemble_rag_response(claim, docs):
     """
    Mock RAG: compose a short verdict and micro-lesson from the docs.
    Replace with a Vertex LLM call that is sent the claim + docs.
    """
     if not docs:
        return {
            "verdict": "Unverified",
            "confidence": 0.35,
            "evidence": [],
            "bullets": ["No matching fact-check found in the local index."],
            "micro_lesson": "When no credible corroboration exists, treat the claim cautiously and check authoritative sources."
        }

    # if any doc says 'False' return Likely False
     for d in docs:
        if d.get("verdict","").lower() == "false":
            return {
                "verdict": "Likely False",
                "confidence": 0.85,
                "evidence": [{"id": d["id"], "url": d["url"], "excerpt": d["article_text"][:250]} for d in docs],
                "bullets": [
                    f"Claim matched fact-check from {docs[0]['source']}.",
                    "No independent corroboration from reliable sources."
                ],
                "micro_lesson": "False context or fabricated claim: always check dates & original sources."
            }

    # otherwise unverified
     return {
        "verdict": "Unverified",
        "confidence": 0.5,
        "evidence": [{"id": d["id"], "url": d["url"], "excerpt": d["article_text"][:250]} for d in docs],
        "bullets": ["Found related content, but no definitive verdict."],
        "micro_lesson": "Look for ClaimReview or multiple independent outlets to confirm."
    }

@app.route("/analyze", methods=["POST"])
def analyze():
    """
    Request JSON: { "text": "<claim or article>", "mode": "mock" or "vertex(optional)" }
    Response JSON: structured result with verdict, evidence, bullets, micro_lesson.
    """
    print("Request method:",request.method)
    print("Request data:",request.get_json())
    data = request.get_json(force=True)
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided."}), 400

    claim = extract_claim(text)
    # Choose mode
    if MODE == "vertex" or data.get("mode") == "vertex":
        # Placeholder for Vertex integration
        # See vertex_integration_example.py for real code.
        result = {
        "verdict": "Unverified",
        "confidence": 0.45,
        "evidence": [],
        "bullets": ["Vertex integration not configured."],
        "micro_lesson": "Enable Vertex AI and set credentials to use real model."
    }
    else:
        docs = local_vector_search(claim)
        result = assemble_rag_response(claim, docs)

    response = {
        "claim": claim,
        "result": result
    }
    return jsonify(response), 200

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json(force=True)
    # store feedback somewhere (file/DB). Here we just echo.
    return jsonify({"status":"ok", "received": data}), 200

if __name__ == "__main__":
    app.run(port=5001, debug=True)
