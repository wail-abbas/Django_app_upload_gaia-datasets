from django.urls import path
from . import views

urlpatterns = [

    path('upload/', views.experimentfile.as_view(), name='upload'),
    path('show_data/', views.show_data, name='show_data'),
    #path('uploaded/', views.uploaded, name='uploaded'),
    
]