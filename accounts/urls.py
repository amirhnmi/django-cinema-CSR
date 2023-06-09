from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterApiView.as_view(), name="register"),
    path("login/", views.LoginApiView.as_view(), name="login"),
    path("user/", views.UserDetailView.as_view(), name="user"),

    path("forget_password/",views.ForgetPasswordView.as_view(),name="forget_password"),
    path("password_reset/",views.PasswordResetView.as_view(),name="password_reset"),
]