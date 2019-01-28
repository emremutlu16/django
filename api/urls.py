from django.urls import path
from api import views

urlpatterns = [
    path('', views.StudentView.as_view(), name='student'),
    path('randomuser', views.RandomUserView.as_view(), name='randomuser')

]
