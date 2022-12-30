
from django.contrib import admin
from django.urls import path , include

from integrant.views import create_integrants,list_integrants
                            
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-integrants/',create_integrants),
    path('list-integrants/',list_integrants)
    
]

