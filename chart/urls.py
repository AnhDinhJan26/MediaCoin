from django.urls import path
from chart.views import Index, GetData

urlpatterns = [
    path('', Index, name='index'),
    path('data', GetData, name='data'),

]
