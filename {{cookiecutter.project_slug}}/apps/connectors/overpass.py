import time
import httpx
from typing import List, Dict, Any

OVERPASS_ENDPOINTS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]

def run_overpass_query(query: str, timeout_seconds: int = 120) -> List[Dict[str, Any]]:
    for endpoint in OVERPASS_ENDPOINTS:
        try:
            with httpx.Client(timeout=timeout_seconds) as client:
                res = client.post(endpoint, data={"data": query}, headers={"User-Agent": "HATStack/1.0"})
                if res.status_code == 200:
                    return res.json().get("elements", [])
        except Exception:
            continue
    return []
