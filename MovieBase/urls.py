from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movieapp import views

router = routers.DefaultRouter()
router.register('api/persons', views.PersonView)
router.register('api/movies', views.MovieView)
router.register('api/users', views.UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
