from django.contrib import admin
from django.urls import path
from YumYum import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('starters/', views.starters, name="starters"),
    path('maincourse/', views.maincourse, name="maincourse"),
    path('desserts/', views.desserts, name='desserts'),
    path('gelatos/', views.gelatos, name="gelatos"),
    path('mocktails/', views.mocktails, name="mocktails"),
    path('shakes/', views.shakes, name="shakes"),
    path('indian/', views.indian, name="indian"),
    path('chinese/', views.chinese, name="chinese"),
    path('american/', views.american, name="american"),
    path('booking/', views.booking, name="booking"),
    path("bookingdata/", views.bookingdata, name="bookingdata"),
    path('check_availability/', views.check_availability, name='check_availability'),
    path('submit_review/', views.submit_review, name='submit_review'),
    path('update-cart/', views.update_cart, name='update_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
