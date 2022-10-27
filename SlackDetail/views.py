from django.shortcuts import render
from django.http import JsonResponse
from .models import SlackDetail
from .serializer import DetailSerializer

def Detail(request):
    detail = SlackDetail.objects.all()
    serializer = DetailSerializer(detail, many=True)
    return JsonResponse(serializer.data, safe=False)
