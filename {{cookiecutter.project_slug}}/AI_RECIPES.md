# 📖 AI CODE RECIPES (Few-Shot Prompting Library)
Use these exact canonical implementations when generating new features.

---

### Recipe 1: HTMX View & Partial Swapping Pattern
```python
# apps/pages/views.py
from django.shortcuts import render

def search_items_view(request):
    query = request.GET.get("q", "").strip()
    items = Item.objects.filter(name__icontains=query) if query else Item.objects.all()
    context = {"items": items, "query": query}
    
    if request.htmx:
        return render(request, "partials/item_list.html", context)
    return render(request, "pages/search.html", context)
```

### Recipe 2: Alpine.js DaisyUI Modal
```html
<div x-data="{ open: false }">
    <button @click="open = true" class="btn btn-primary">Detayları Gör</button>

    <div x-show="open" x-cloak class="modal modal-open">
        <div class="modal-box" @click.outside="open = false">
            <h3 class="font-bold text-lg">Başlık</h3>
            <p class="py-4">İçerik buraya gelir.</p>
            <div class="modal-action">
                <button @click="open = false" class="btn">Kapat</button>
            </div>
        </div>
    </div>
</div>
```

### Recipe 3: Django Form with widget_tweaks & DaisyUI
```html
{% raw %}{% load widget_tweaks %}
{% load honeypot %}

<form hx-post="{% url 'inquiries:submit' %}" hx-target="#form-box" hx-swap="outerHTML" class="space-y-4">
    {% csrf_token %}
    {% render_honeypot_field %}
    
    <div class="form-control">
        <label class="label"><span class="label-text font-semibold">Adınız</span></label>
        {% render_field form.name class="input input-bordered w-full" placeholder="Ad Soyad" %}
        {% if form.name.errors %}
            <span class="text-error text-xs mt-1">{{ form.name.errors.0 }}</span>
        {% endif %}
    </div>

    <button type="submit" class="btn btn-primary w-full">
        <span class="htmx-indicator loading loading-spinner loading-xs"></span>
        <span>Gönder</span>
    </button>
</form>{% endraw %}
```

### Recipe 4: Toast Feedback Pattern
```python
# In your view:
from django.contrib import messages
messages.success(request, "İşleminiz başarıyla tamamlandı!")
```
Toast is rendered in `templates/components/messages.html` and automatically auto-dismisses after 4 seconds via Alpine.js.
