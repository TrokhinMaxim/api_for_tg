from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status
from .models import CustomUser, CurrencyRequest, Text
from .serializers import (
    CustomUserSerializer,
    CurrencySerializer,
    CurrencyRequestHistorySerializer,
    SubscriptionSerializer,
    CurrencyTemplateSerializer,
    GreetingSerializer,
    UserHistoryTemplateSerializer,
)
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


from .dollar_currency import get_currency


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class UserProfileView(RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        if self.request.user.is_staff:
            user_id = self.kwargs.get("user_id")
            return get_object_or_404(CustomUser, pk=user_id)
        return self.request.user


class CurrencyAPIView(APIView):
    def get(self, request, *args, **kwargs):
        result = get_currency()
        if "Ошибка" in result:
            return Response(
                {"detail": result}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        serializer = CurrencySerializer(data=result)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"detail": "Неверный формат данных"}, status=status.HTTP_400_BAD_REQUEST
            )


class CurrencyRequestHistoryView(generics.ListAPIView):
    serializer_class = CurrencyRequestHistorySerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return CurrencyRequest.objects.filter(user_id=user_id)


class SubscribeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.active_follow = True
        user.save()
        serializer = SubscriptionSerializer(user)
        return Response(
            {"message": "Вы успешно подписались на рассылку курса."},
            status=status.HTTP_200_OK,
        )


class UnsubscribeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        user.active_follow = False
        user.save()
        serializer = SubscriptionSerializer(user)
        return Response(
            {"message": "Вы успешно отписались от рассылки курса."},
            status=status.HTTP_200_OK,
        )


class GreetingView(APIView):
    def get(self, request, *args, **kwargs):
        username = request.user.username if request.user.is_authenticated else "Guest"
        greeting_text = Text.objects.get(name="greeting_text").content
        personalized_greeting = greeting_text.format(username=username)
        return Response({"text": personalized_greeting})


class CurrencyTemplateView(APIView):
    def get(self, request, *args, **kwargs):
        currency_data = get_currency()
        val = currency_data["exchange_rate"]
        template_text = Text.objects.get(name="currency_template").content
        formatted_text = template_text.format(val=val)
        return Response({"text": formatted_text})


class UserHistoryTemplateView(generics.ListAPIView):
    serializer_class = UserHistoryTemplateSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user_username = self.kwargs.get("user_username")
        user = get_user_model().objects.get(username=user_username)
        return CurrencyRequest.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        template_text = Text.objects.get(name="user_history_template").content
        user_requests_text = " ".join(
            [
                f'Курс {item["exchange_rate"]} на {item["date"]}.'
                for item in serializer.data
            ]
        )
        formatted_text = template_text.format(user_requests=user_requests_text)

        return Response({"text": formatted_text})
