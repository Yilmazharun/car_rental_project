from django.urls import path
from reservations.api import views

urlpatterns = [
    path("add/auth/", views.ReservationCreateAPIView.as_view(), name="car_user_add_reserv"),
    path("add/", views.ReservationCreateAPIView.as_view(), name="car_add_reserv"),
    path("auth/", views.ReservationAvailabilityAPIView.as_view(), name="reserv_availability"),
    path("<int:pk>/auth/", views.ReservationDetailAPIView.as_view(), name="reserv_detail_auth"),
    path("<int:pk>/admin/", views.ReservationDetailAPIView.as_view(), name="reserv_detail_admin"),
    path("admin/all/", views.ReservationListAll.as_view(), name="list_admin_all"),
    path("auth/all/", views.ReservationListAll.as_view(), name="list_auth"),
    path("admin/auth/all/", views.ReservationListAll.as_view(), name="list_auth_admin"),
    path("admin/all/pages/", views.ReservationListAll.as_view(), name="list_pages_admin"),
    path("admin/<int:pk>/auth/", views.ReservationDeleteAPIView.as_view(), name="reserv_delete"),
    path("admin/auth/", views.ReservationUpdateAPIView.as_view(), name="reserv_update"),
]