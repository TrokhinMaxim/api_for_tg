from django.urls import path
from .views import (
    RegisterUserView,
    UserProfileView,
    CurrencyAPIView,
    CurrencyRequestHistoryView,
    SubscribeView,
    UnsubscribeView,
    GreetingView,
    CurrencyTemplateView,
    UserHistoryTemplateView,
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),
    path("user/profile/", UserProfileView.as_view(), name="user-profile"),
    path(
        "user/profile/<int:user_id>/",
        UserProfileView.as_view(),
        name="admin-user-profile",
    ),
    path("auth/token/", obtain_auth_token, name="auth-token"),
    path("get_currency/", CurrencyAPIView.as_view(), name="get_currency"),
    path(
        "history/<int:user_id>/",
        CurrencyRequestHistoryView.as_view(),
        name="currency_request_history",
    ),
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("unsubscribe/", UnsubscribeView.as_view(), name="unsubscribe"),
    path("greeting/", GreetingView.as_view(), name="greeting"),
    path(
        "currency_template/", CurrencyTemplateView.as_view(), name="currency_template"
    ),
    path(
        "user_history_template/<str:user_username>/",
        UserHistoryTemplateView.as_view(),
        name="user_history_template",
    ),
]
