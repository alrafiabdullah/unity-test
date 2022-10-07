from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Index(APIView):
    def get(self, request):
        return Response("GET success!", status=status.HTTP_200_OK)

    def post(self, request):
        return Response("POST success!", status=status.HTTP_201_CREATED)

    def put(self, request):
        return Response("PUT success!", status=status.HTTP_200_OK)

    def delete(self, request):
        return Response("DELETE success!", status=status.HTTP_200_OK)
