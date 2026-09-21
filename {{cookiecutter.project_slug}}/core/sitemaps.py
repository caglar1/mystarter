from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['pages:home', 'pages:about', 'pages:services', 'pages:contact']

    def location(self, item):
        return reverse(item)
