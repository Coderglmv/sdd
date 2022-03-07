from django.urls import path
from .views import about_us, main, shopView, bookView, database
app_name = 'cofe'

urlpatterns = [
    path('', main, name='main'),
    path('about_us/',  about_us, name='about_us'),
    path('shop/',  shopView, name='shop'),
    path('book/<int:pk>/',  bookView, name='book'),
    path('database/',  database, name='database'),

]