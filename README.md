# 🚀 AI-Native Django HAT Stack Cookiecutter

> **Django 5.1 + HTMX + Alpine.js + Tailwind CSS & DaisyUI + Lucide Icons + SortableJS + Leaflet + PWA**

Modern, ultra hafif ve yüksek performanslı iş uygulamaları geliştirmek için tasarlanmış; **Antigravity, Cursor, Windsurf, Claude Code** gibi yapay zeka ajanlarıyla %100 uyumlu **AI-Native Cookiecutter Proje Başlatıcı**.

---

## ✨ Neden Bu Starter Pack?

* ⚡ **Zero-Node.js:** Tailwind CSS derlemesi dahil hiçbir aşamada Node.js veya `npm` gerekmez. Standalone Tailwind CLI kullanılır.
* 📦 **100% Self-Hosted Assets:** HTMX, Alpine, DaisyUI, Lucide, Leaflet ve SortableJS yerel olarak `static/vendor/` altındadır. Dış CDN kesintisi veya KVKK/GDPR riski yoktur.
* 🤖 **AI-Native Mimarisi:** 
  * Dinamik `.cursorrules` ve `AI_INSTRUCTIONS.md`
  * `AI_RECIPES.md` ile AI ajanına hazır few-shot kod kalıpları
  * `python manage.py seed_demo_data` ile anında test verisi üretimi
  * Canlı bileşen rehberi: `/dev/ui-kit/`
* 🛡️ **Hazır İşlevler:** CSRF otomatik enjeksiyonu, honeypot spam tuzağı, DaisyUI 4s otomatik kapanan toast bildirimleri, skeleton yükleme durumları.

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
*(GitHub'a yükledikten sonra: `cookiecutter gh:kullanici-adiniz/starterpack`)*

### 3. Etkileşimli Seçenekler
| Seçenek | Varsayılan | Açıklama |
| :--- | :---: | :--- |
| `project_name` | My Business App | Projenizin adı |
| `project_slug` | my_business_app | Klasör ve Python paket adı |
| `include_leaflet_maps` | y | Leaflet.js ve Stadia/Carto harita katmanı |
| `include_llm_gateway` | y | 12-Factor Universal httpx AI Gateway |
| `include_news_scraper` | n | RSS Feed & newspaper4k makale kazıyıcı |
| `include_kanban` | y | SortableJS dokunmatik sürükle-bırak Kanban |
| `include_dev_ui_kit` | y | `/dev/ui-kit/` canlı stil ve bileşen vitrini |
| `default_database` | sqlite | SQLite (hızlı geliştirme) veya PostgreSQL |

---

## 🏃‍♂️ Oluşturulan Projeyi Başlatma

```bash
# 1. Proje dizinine geçin
cd <proje_adiniz>

# 2. Sanal ortamı kurun ve aktif edin
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

## 🐳 Docker ile Canlıya Alma (Production)

Çoklu mimari (x86_64 ve ARM64/Apple Silicon) destekli Dockerfile hazırdır:

```bash
docker compose up -d --build
```
