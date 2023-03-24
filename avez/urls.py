from django.urls import path


from . import views

# Endpoints
urlpatterns = [
    path('aves', views.Aves.as_view(), name='Aves')
]