from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('series/', views.series, name='series'),
    path('series/<slug:serie>/', views.serie_view, name='serie_view'),
    path('series/<slug:serie>/<slug:post>/', views.serie_post, name='serie_post'),

    path('<slug:type>/', views.type_view, name='type_view'),
    path('<slug:type>/<slug:category>/', views.category_view, name='category_view'),
    path('<slug:type>/<slug:category>/<slug:post>/', views.post_page, name='post_page'),
]
