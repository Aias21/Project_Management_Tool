from django.urls import path
from pmt.views import log_in


app_name = 'pmt'
urlpatterns = [
    path('', log_in, name='login')
]