from django.urls import path
from . import views
urlpatterns = [
    path('central/', views.site_list),
]
