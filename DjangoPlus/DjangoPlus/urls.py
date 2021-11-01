from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)