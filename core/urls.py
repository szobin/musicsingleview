from django.urls import include, path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'singles', views.SingleViewSet, basename="single")

urlpatterns = [
    path('', include((router.urls, 'core'), namespace='core')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-get-sv/<str:pk>/', views.SingleView.as_view()),
]