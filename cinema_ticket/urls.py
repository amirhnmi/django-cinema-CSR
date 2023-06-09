
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('categories/screening/', include('screenings.urls')),
    path('categories/theater/', include('theater.urls')),
    path('categories/artandexpriens/', include('artAndExpriens.urls')),
    path('categories/childrenstheater/', include('childrenTheater.urls')),
    path('categories/comedytheater/', include('comedyTheater.urls')),
    path('news/', include('news.urls')),
    path('salestable/', include('salesTable.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)