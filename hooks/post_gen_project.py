import os
import shutil
from pathlib import Path

PROJECT_ROOT = Path(os.getcwd())

def remove_path(path_str):
    p = PROJECT_ROOT / path_str
    if p.is_dir():
        shutil.rmtree(p, ignore_errors=True)
    elif p.is_file():
        p.unlink(missing_ok=True)

# 1. Maps cleanup
if "{{ cookiecutter.include_leaflet_maps }}" != "y":
    remove_path("templates/components/map.html")
    remove_path("apps/connectors/geo_utils.py")
    remove_path("apps/connectors/overpass.py")
    remove_path("apps/connectors/management/commands/sync_overpass.py")
    remove_path("static/vendor/leaflet")

# 2. LLM Gateway cleanup
if "{{ cookiecutter.include_llm_gateway }}" != "y":
    remove_path("apps/connectors/llm.py")

# 3. News Scraper cleanup
if "{{ cookiecutter.include_news_scraper }}" != "y":
    remove_path("apps/connectors/news_enrichment.py")
    remove_path("apps/connectors/news_pipeline.py")
    remove_path("apps/connectors/management/commands/sync_news.py")

# 4. Kanban cleanup
if "{{ cookiecutter.include_kanban }}" != "y":
    remove_path("templates/components/kanban_column.html")
    remove_path("static/vendor/sortable")

# 5. UI Kit cleanup
if "{{ cookiecutter.include_dev_ui_kit }}" != "y":
    remove_path("templates/pages/ui_kit.html")

print("\n\033[92m[✓] Projeniz '{{ cookiecutter.project_name }}' basariyla olusturuldu!\033[0m")
print("Baslamak icin:")
print("  cd {{ cookiecutter.project_slug }}")
print("  python3 -m venv venv && source venv/bin/activate")
print("  pip install -r requirements.txt")
print("  python manage.py migrate")
print("  python manage.py seed_demo_data")
print("  python manage.py runserver\n")
