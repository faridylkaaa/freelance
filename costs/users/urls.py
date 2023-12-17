from django.urls import path
from costs.users import views

urlpatterns = [path('login/', views.LoginPerson.as_view(), name='login'),
               path('create/', views.CreatePerson.as_view(), name='create'),
               path('logout/', views.logout_user, name='logout')]