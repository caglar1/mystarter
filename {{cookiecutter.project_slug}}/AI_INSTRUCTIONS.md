# 🤖 AI AGENT DIRECTIVE & ARCHITECTURE GOVERNANCE
# Project: {{ cookiecutter.project_name }}

Welcome, AI Engineer. You are pair programming on **{{ cookiecutter.project_name }}**.
You must adhere strictly to the **HAT Stack** architecture outlined below.

## 1. ARCHITECTURE FOUNDATION
* **Backend:** Python 3.12 + Django 5.1
* **Frontend AJAX:** HTMX (`hx-get`, `hx-post`, `hx-target`, `hx-swap`)
* **Local UI State:** Alpine.js (`x-data`, `x-show`, `x-init`, modals, drawers, toasts)
* **Styling:** Tailwind CSS 3.4 + DaisyUI 4.12 (Zero Node.js dependency)
* **Icons:** Lucide Icons (`<i data-lucide="..."></i>` with `lucide.createIcons()` on `htmx:afterSwap`)
* **Feedback:** DaisyUI Toasts auto-dismissed in 4 seconds via Alpine.js

## 2. KEY REPOSITORY RULES
1. **Always Check if request.htmx:** When writing views, return partial HTML snippets when `request.htmx` is True, and full pages when False.
2. **DaisyUI Semantic Classes:** Use `btn btn-primary`, `card`, `alert`, `modal`, `input input-bordered`. Do not invent non-existent CSS utility classes. Refer to `/dev/ui-kit/` for exact patterns.
3. **No External CDNs:** Core vendor files are local under `static/vendor/`.
4. **Data Verification:** Use `python manage.py seed_demo_data` to populate mock records when verifying features.
