from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoListAndCreate.as_view()),
    path('<int:pk>/', views.TodoShowUpdateAndDestroy.as_view())
]
