from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ml import views

router = routers.DefaultRouter()
router.register(r'predictions', views.ResultView, 'prediction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('results/', views.predict),
]
