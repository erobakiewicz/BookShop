from django.urls import path, include

from accounts.views import UpdateUserView, CreateUserView, UserProfileView, ChangePasswordView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("user/<int:pk>", UpdateUserView.as_view(), name='userchange'),
    path("userprofile/<int:pk>", UserProfileView.as_view(), name="userprofile"),
    path("changepassword/", ChangePasswordView.as_view(), name="changepassword"),
    path("registration/", CreateUserView.as_view(), name="registration"),

]
