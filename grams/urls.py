"""

    To Do - dev:
    1. Add all app configs to settings.py in INSTALLED_APPS

    To Do - before deployment:
    1. Remove all comments
    2. Minify CSS & JS files

"""


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('assets/', include('assets.urls')),
    path('transactions/', include('transactions.urls')),
    path('branch/', include('branch.urls')),
    path('company/', include('company.urls')),
    path('vendors/', include('vendors.urls')),
    path('assetbrands/', include('assetBrands.urls')),
    path('assetcategories/', include('assetCategories.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
