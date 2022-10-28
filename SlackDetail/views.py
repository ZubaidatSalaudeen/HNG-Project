from django.shortcuts import render
from django.http import JsonResponse
from .models import SlackDetail
from .serializer import DetailSerializer
from rest_framework.decorators import api_view

@api_view(["GET"])
def Detail(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin":"*"}
    detail = SlackDetail.objects.all()
    serializer = DetailSerializer(detail, many=True)
    return JsonResponse(serializer.data, safe=False)
