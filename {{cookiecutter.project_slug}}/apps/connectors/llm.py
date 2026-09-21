import os
import httpx
from typing import Optional, Dict, Any, List

class LLMClient:
    """Universal pure httpx LLM client supporting OpenRouter, DeepSeek, Gemini, Claude, OpenAI."""

    @staticmethod
    def _extract_text(data: Dict[str, Any]) -> str:
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        elif "content" in data and isinstance(data["content"], list) and len(data["content"]) > 0:
            return data["content"][0]["text"]
        raise ValueError(f"Unrecognized LLM response structure: {data}")

    @classmethod
    def generate(
        cls,
        prompt: str,
        system_prompt: str = "",
        model: Optional[str] = None,
        effort: str = "low",
        timeout: float = 60.0
    ) -> str:
        url = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1/chat/completions")
        key = os.getenv("LLM_API_KEY", "")
        target_model = model or os.getenv("LLM_MODEL", "anthropic/claude-3.5-sonnet")

        headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        messages = [{"role": "system", "content": system_prompt}] if system_prompt else []
        messages.append({"role": "user", "content": prompt})
        payload = {"model": target_model, "messages": messages, "temperature": 0.2}

        with httpx.Client(timeout=timeout) as client:
            res = client.post(url, headers=headers, json=payload)
            res.raise_for_status()
            return cls._extract_text(res.json())
