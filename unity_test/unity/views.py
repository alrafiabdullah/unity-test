from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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
    def get(self, request):
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
        email_subscription = EmailSubscription.objects.get(
            email=request.data["email"])
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
