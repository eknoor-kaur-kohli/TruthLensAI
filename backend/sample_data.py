# sample_data.py
# small JSONL-like Python list; used for local vector-search stub
SAMPLE_FACT_CHECKS = [
    {
        "id": "1",
        "claim": "Drinking hot water cures COVID-19",
        "verdict": "False",
        "source": "Alt News",
        "url": "https://altnews.example/hot-water-covid",
        "article_text": "Medical authorities state that drinking hot water does not cure COVID-19..."
    },
    {
        "id": "2",
        "claim": "5G towers caused coronavirus",
        "verdict": "False",
        "source": "FactCheck.org",
        "url": "https://factcheck.example/5g-corona",
        "article_text": "No evidence connects 5G networks to spread of viruses..."
    }
]
