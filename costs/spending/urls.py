from django.urls import path
from costs.spending import views


urlpatterns = [
    path('create/', views.SpendingCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.SpendingUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.SpendingDeleteView.as_view(), name='delete'),
    path('', views.IndexSpendingsView.as_view(), name='index')
]