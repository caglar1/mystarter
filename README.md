# 🚀 AI-Native Django HAT Stack Cookiecutter

> **Django 5.1 + HTMX + Alpine.js + Tailwind CSS & DaisyUI + Lucide Icons + SortableJS + Leaflet + PWA**

Modern, ultra hafif ve yüksek performanslı iş uygulamaları geliştirmek için tasarlanmış; **Antigravity, Cursor, Windsurf, Claude Code** gibi yapay zeka ajanlarıyla %100 uyumlu **AI-Native Cookiecutter Proje Başlatıcı**.

---

## ✨ Neden Bu Starter Pack?

* ⚡ **Zero-Node.js:** Tailwind CSS derlemesi dahil hiçbir aşamada Node.js veya `npm` gerekmez. Standalone Tailwind CLI kullanılır.
* 📦 **100% Self-Hosted Assets:** HTMX, Alpine, DaisyUI, Lucide, Leaflet ve SortableJS yerel olarak `static/vendor/` altındadır. Dış CDN kesintisi veya KVKK/GDPR riski yoktur.
* 🤖 **AI-Native Mimarisi:** 
  * Dinamik `.cursorrules` ve `AI_INSTRUCTIONS.md` (seçilen modüllere göre otomatik şekillenir)
  * `AI_RECIPES.md` ile AI ajanına hazır few-shot kod kalıpları
  * `python manage.py seed_demo_data` ile anında test verisi üretimi
  * Canlı bileşen rehberi: `/dev/ui-kit/`
* 🛡️ **Hazır İşlevler:** CSRF otomatik enjeksiyonu, honeypot spam tuzağı, DaisyUI 4s otomatik kapanan toast bildirimleri, skeleton yükleme durumları.
* 🚀 **Dahili WhiteNoise:** Ek bir Nginx statik ayarına gerek kalmadan, Gzip/Brotli sıkıştırmalı ve cache-busting özellikli kurumsal statik dosya sunumu varsayılan olarak devrededir.

---

## 🛠️ Kurulum ve Yeni Proje Oluşturma

### 1. Cookiecutter'ı Yükleyin (Gerekliyse)
```bash
pip install cookiecutter
```

### 2. Şablonu Çalıştırın
Yerel klasör üzerinden:
```bash
cookiecutter /Users/caglar/Desktop/starterpack
```
*(Veya doğrudan GitHub'dan: `cookiecutter gh:caglar1/mystarter`)*

### 3. Etkileşimli Seçenekler
| Seçenek | Varsayılan | Açıklama |
| :--- | :---: | :--- |
| `project_name` | My Business App | Projenizin adı |
| `project_slug` | my_business_app | Klasör ve Python paket adı |
| `include_leaflet_maps` | y | Leaflet.js ve harita katmanı + pure Python Haversine matematiği |
| `include_llm_gateway` | y | 12-Factor Universal httpx AI Gateway |
| `include_news_scraper` | n | RSS Feed & newspaper4k makale kazıyıcı pipeline |
| `include_kanban` | y | SortableJS dokunmatik sürükle-bırak Kanban bileşeni |
| `include_dev_ui_kit` | y | `/dev/ui-kit/` canlı stil ve bileşen vitrini |
| `default_database` | sqlite | SQLite (hızlı geliştirme) veya PostgreSQL |

---

## 🏃‍♂️ Oluşturulan Projeyi Başlatma

```bash
# 1. Proje dizinine geçin
cd <proje_adiniz>

# 2. Sanal ortamı kurun ve aktif edin (Python 3.11 veya 3.12 önerilir)
python3 -m venv venv
source venv/bin/activate

# 3. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 4. Ortam değişkenlerini oluşturun
cp .env.example .env

# 5. Veritabanını hazırlayın ve demo verileri basın
python manage.py migrate
python manage.py seed_demo_data

# 6. Geliştirme sunucusunu başlatın
python manage.py runserver
```

Tarayıcınızda açın:
* 🌐 **Ana Sayfa:** `http://127.0.0.1:8000/`
* 🎨 **Canlı UI Kit:** `http://127.0.0.1:8000/dev/ui-kit/`
* ⚙️ **Django Admin:** `http://127.0.0.1:8000/admin/`

---

## 🔍 Mimari & Katman Detayları (Deep Dive)

### 1. 🗺️ Harita Katmanı ve Karo (Tile) Mimarisi
* **Self-Hosted Kütüphane:** Leaflet `1.9.4` JS, CSS ve pin görselleri tamamen yerel `static/vendor/leaflet/` altından sunulur.
* **Karo (Tile) Sağlayıcıları:**
  * **Geliştirme & Varsayılan:** API anahtarı gerektirmeyen ücretsiz **CARTO Positron** CDN (`light_all`) kullanılır.
  * **SLA ve Kurumsal:** Dilerseniz `.env` içinde `STADIA_MAPS_API_KEY` tanımlayarak **Stadia Maps (Alidade Smooth)** katmanına geçebilirsiniz.
  * **Milyonluk Trafik (Sıfır Maliyet):** Harita verisini tek bir `.pmtiles` arşivine dönüştürüp **Cloudflare R2** (çıkış trafiği $0) üzerine koyarak sınırsız haritayı sunucu maliyetsiz dağıtabilirsiniz.
* **Alpine.js İzolasyonu:** Harita, Alpine `$refs.mapContainer` içine kapsüllenmiştir; böylece dinamik HTMX sayfa geçişlerinde container referansı kaybolmaz ve bellek sızıntısı yaşanmaz.

### 2. 🤖 Universal LLM Gateway (`apps.connectors.llm.LLMClient`)
Ağır SDK'lar (`openai`, `langchain`, `litellm`) yerine saf Python ve `httpx` ile çalışan 12-Factor REST gateway:
* **Desteklenen Sağlayıcılar:** OpenRouter, Anthropic Claude, OpenAI, DeepSeek, Google Gemini, Qwen, Groq.
* **Gerekli `.env` Değişkenleri:**
  ```ini
  LLM_BASE_URL=https://openrouter.ai/api/v1/chat/completions
  LLM_API_KEY=sk-or-v1-...
  LLM_MODEL=anthropic/claude-3.5-sonnet
  ```
* **Reasoning Bütçelemesi:** `effort="none" | "low" | "medium" | "high"` parametresi sayesinde Claude 3.7 / OpenAI o-serisi modellerinde düşünme jetonları otomatik yönetilir.

### 3. 🔎 Hibrit Arama Motoru (PostgreSQL FTS + SQLite Fallback)
Harici arama sunucularına (Elasticsearch, Meilisearch) gerek bırakmayan akıllı mimari:
* **Canlıda (PostgreSQL):** `django.contrib.postgres.search` üzerinden A/B/C ağırlıklı `SearchVector`, `websearch` sorguları ve `SearchRank` ile relevance skoru hesaplar.
* **Geliştirmede (SQLite):** Geliştirme ortamında PostgreSQL zorunluluğu getirmeden, güvenli ve hızlı `icontains` fallback'i ile sıfır konfigürasyonla çalışır.

### 4. 📦 Statik Dosyalar & WhiteNoise
* Canlı ortamda Nginx reverse proxy arkasında veya doğrudan Gunicorn ile çalışırken statik dosyalar **WhiteNoise** ile optimize sunulur.
* Gzip ve Brotli sıkıştırma, benzersiz hash'li dosya isimleri (cache-busting) ve `WHITENOISE_MANIFEST_STRICT = False` güvenlik supabı hazırdır.

---

## 🐳 Docker ile Canlıya Alma (Production)

Çoklu mimari (x86_64 ve ARM64/Apple Silicon) destekli Dockerfile hazırdır:

```bash
docker compose up -d --build
```
