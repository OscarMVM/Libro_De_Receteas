from django.shortcuts import render
from .models import Client
from rest_framework.views import APIView
from .serializers import postSerializer
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


# Create your views here.

# def index(request):
#     # return HttpResponse('Hello from Python!')
#     return render(request, "index.html")

class AllPost(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        allpost = Client.objects.order_by('id')
        serializer = postSerializer(allpost, many=True)
        return Response(serializer.data)


