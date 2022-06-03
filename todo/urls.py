import imp
from django.urls import path
from .views import TodoCreate, TodoDelete, TodoDetail, TodoList, TodoUpdate

urlpatterns = [
    path('', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
]
