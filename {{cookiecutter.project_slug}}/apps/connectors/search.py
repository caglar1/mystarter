from django.db import connection
from django.db.models import Q
from typing import Any

def search_news_articles(queryset: Any, search_term: str) -> Any:
    if not search_term or not search_term.strip():
        return queryset

    cleaned_term = search_term.strip()

    if connection.vendor == 'postgresql':
        try:
            from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
            vector = SearchVector('title', weight='A') + SearchVector('full_content', weight='B')
            query = SearchQuery(cleaned_term, search_type='websearch')
            return queryset.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.03).order_by('-rank')
        except Exception:
            pass

    return queryset.filter(
        Q(title__icontains=cleaned_term) | Q(full_content__icontains=cleaned_term)
    )
