from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', views.login, name = 'login'),
    path('<int:pk>/<password>', views.signIn),
    path('<int:pk>', views.AccountDetailView, name = 'account-detail')
]