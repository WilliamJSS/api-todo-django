from django.urls import path

from . import views

urlpatterns = [
    path('', views.getList),
    path('<int:id>/', views.show_update_delete)
]
