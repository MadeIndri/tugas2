from django.urls import path
from todolist.views import register
from todolist.views import login_user
from todolist.views import show_todolist
from todolist.views import logout_user
from todolist.views import createtask
from todolist.views import delete
from todolist.views import change

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
     path('create-task/', createtask, name='create-task'),
    path('delete/<int:pk>', delete, name='delete'),
    path('change/<int:pk>', change, name='change'),
]