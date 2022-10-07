from datetime import datetime

from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import EmailSubscription
from .serializers import EmailSubscriptionSerializer, EmailSubscriptionCRUDSerializer


class Index(APIView):
    def get(self, request):
        return Response({"message": "GET success!"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "POST success!"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        return Response({"message": "PUT success!"}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({"message": "DELETE success!"}, status=status.HTTP_200_OK)


class EmailSubscriptionView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if "email" in request.query_params:
            try:
                email_subscription = EmailSubscription.objects.get(
                    email=request.query_params["email"])
            except:
                return Response({"message": "Email not found"}, status=status.HTTP_400_BAD_REQUEST)
            serializer = EmailSubscriptionSerializer(email_subscription)
            return Response(serializer.data, status=status.HTTP_200_OK)
        email_subscriptions = EmailSubscription.objects.all()
        serializer = EmailSubscriptionSerializer(
            email_subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmailSubscriptionCRUDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            email_subscription = EmailSubscription.objects.get(
                email=request.data["email"])
        except:
            return Response({"message": "Email not found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = EmailSubscriptionCRUDSerializer(
            email_subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            email = request.data["email"]
        except:
            return Response({"message": "Email not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            email_subscription = EmailSubscription.objects.get(
                email=email)
        except:
            return Response({"message": "Email not found"}, status=status.HTTP_400_BAD_REQUEST)
        email_subscription.delete()
        return Response({"message": "Email subscription deleted"}, status=status.HTTP_200_OK)


# HTML Views
def subscribe_view(request):
    all_subscriptions = EmailSubscription.objects.all().order_by("-created_at")
    this_month_subscriptions = EmailSubscription.objects.filter(
        created_at__month=datetime.now().month).order_by("-created_at").count()
    unsubscribed_count = EmailSubscription.objects.filter(
        is_subscribed=False).count()

    context = {
        "subscriptions": all_subscriptions,
        "this_month_subscriber_count": this_month_subscriptions,
        "unsubscribed_count": unsubscribed_count,
    }
    return render(request, 'unity/subscribe.html', context)
