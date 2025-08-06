from django.contrib import admin
from django.urls import path
from drc_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drc-queries/', views.drc_query_examples),  # For demo queries
]
