from django.shortcuts import render
from django.http import JsonResponse
from .models import SlackDetail
from .serializer import DetailSerializer
from rest_framework.decorators import api_view

@api_view(["GET"])
def Detail(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin":"*"}
    detail = {"slackUsername":"zubaidatsalaudeen", "backend":True, "age":21,
               "bio":"A tech enthusiast and a biginner level backend developer"}
    return JsonResponse(detail, headers=header)