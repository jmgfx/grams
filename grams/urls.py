from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('user/', include('users.urls')),
    path('assets/', include('assets.urls')),
    path('transactions/', include('transactions.urls')),
    path('branch/', include('branch.urls')),
    path('company/', include('company.urls')),
    path('vendors/', include('vendors.urls')),
    path('assetbrands/', include('assetBrands.urls')),
    path('assetcategories/', include('assetCategories.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
