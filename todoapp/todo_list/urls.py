from django.urls import path, include
from todo_list import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.ListTodo.as_view(), name='list'),
    path('<int:pk>', views.DetailsTodo.as_view(), name='details'),
    path('create/', views.CreateTodo.as_view(), name='createtodo'),
    path('update/<int:pk>', views.UpdateTodo.as_view(), name='updatetodo'),
    path('delete/<int:pk>', views.DeleteTodo.as_view(), name='deletetodo'),
    path('listallorone/', views.ListAllOrOne.as_view(), name="lsitallorone")
 ]