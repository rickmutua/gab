from django.urls import path, include
from . import views

from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('category/<str:category_id>/<slug:category_slug>/', views.single_category, name='single-category'),
    path('<str:box_id>/<slug:box_slug>/', views.box, name='box'),

    path('add-to-cart/<str:box_id>/<slug:box_slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<str:box_id>/<slug:box_slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('cart/', views.display_cart, name='cart'),

    path('checkout/', views.checkout, name='checkout')
]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)