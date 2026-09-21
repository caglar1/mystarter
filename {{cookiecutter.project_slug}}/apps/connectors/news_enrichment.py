import json
from typing import Dict, Any

def enrich_news_article(title: str, content: str, default_category: str = "general") -> Dict[str, Any]:
    # Returns structured metadata structure for article
    return {
        "tldr": [f"{title} hakkında özet bilgi."],
        "category": default_category,
        "sentiment": "neutral",
        "importance_score": 5,
        "tags": [default_category]
    }
