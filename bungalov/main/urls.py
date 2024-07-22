from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('bungalov1/', views.b1, name='b1'),
    path('bungalov2/', views.b2, name='b2'),
    path('bungalov3/', views.b3, name='b3'),
    path('bungalov4/', views.b4, name='b4'),
    path('bungalov5/', views.b5, name='b5'),
    path('bungalov6/', views.b6, name='b6'),
    path('bungalov7/', views.b7, name='b7'),
    path('bungalov8/', views.b8, name='b8'),
    path('kurallar/', views.kurallar, name='kurallar'),
    path('about', views.about, name='hak'),
    path('bungalov/', views.bg, name='bg'),
    path('bungalov10/', views.bg2, name='bg2'),
    path('bungalov11/', views.bg3, name='bg3'),
    path('bungalov12/', views.bg4, name='bg4'),
    path('villa/', views.villa, name='villa'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)