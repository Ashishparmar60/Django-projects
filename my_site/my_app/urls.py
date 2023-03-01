from django.urls import path
from .views import thank_you, review_form, list, delete, home

app_name = 'my_app'

urlpatterns = [
    path('thank_you/', thank_you, name='thank_you'),
    path('review/', review_form, name='review_form'),
    path('list/', list, name='list'),
    path('delete/', delete, name='delete'),
    path('', home, name='home'),
]