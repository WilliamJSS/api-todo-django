from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoListAndCreate.as_view()),
    path('<int:id>/', views.TodoShowUpdateAndDestroy.as_view())
]
