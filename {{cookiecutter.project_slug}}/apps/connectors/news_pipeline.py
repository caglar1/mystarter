import feedparser
from newspaper import Article
from apps.connectors.news_enrichment import enrich_news_article

def run_news_pipeline(feed_url: str, default_category: str = "tech", max_entries: int = 5):
    feed = feedparser.parse(feed_url)
    processed = []
    for entry in getattr(feed, "entries", [])[:max_entries]:
        link = getattr(entry, "link", None)
        title = getattr(entry, "title", "").strip()
        if not link or not title:
            continue
        full_text = ""
        try:
            art = Article(link)
            art.download(); art.parse()
            full_text = art.text.strip()
        except Exception:
            pass
        if not full_text:
            full_text = getattr(entry, "summary", "") or title
        meta = enrich_news_article(title, full_text, default_category)
        processed.append({"title": title, "link": link, "content": full_text, "meta": meta})
    return processed
