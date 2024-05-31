from django.urls import path
from cars.api import views

urlpatterns = [
    path("admin/<int:imageId>/add/", views.CarAddAPIView.as_view(), name="car_add"),
    path("visitors/<int:pk>/", views.CarDetailAPIView.as_view(), name="car_detail"),
    path("visitors/pages/", views.CarListAPIView.as_view(), name="car_all_pages"),
    path("visitors/all/", views.CarListAPIView.as_view(), name="car_all"),
    path("admin/<int:pk>/auth/", views.CarDeleteAPIView.as_view(), name="car_delete"),
    path("admin/auth/", views.CarUpdateAPIView.as_view(), name="car_update"),
]