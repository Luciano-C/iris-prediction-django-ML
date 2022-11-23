from django.urls import path
from .views import *

#app_name = 'predict'

urlpatterns = [
    path('', predict, name='predict'),
    path('predict/', predict_chances, name='submit_prediction'),
    path('results/', view_results, name='results')
]