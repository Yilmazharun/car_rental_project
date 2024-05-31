from users.api import views
from django.urls import path

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path((""), views.UserListAPIView.as_view(), name="user_personal"),
    path(("auth/all/"), views.UserListAPIView.as_view(), name="user_all"),
    path(("auth/pages/"), views.UserListAPIView.as_view(), name="user_page_all"),
    path(("<int:pk>/auth/"), views.UserDetail.as_view(), name="user_detail_auth"),
    path(("auth/"), views.ChangePasswordView.as_view(), name="change_password"),
]
