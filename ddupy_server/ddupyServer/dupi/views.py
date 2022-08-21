#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .AI.executeAImodel import executeAImodel
from .models import Dupi
from .serializers import DupiSerializer


# https://www.anycodings.com/1questions/1516966/receive-a-base64-encoded-image-in-django-rest-framework-and-save-into-imagefield 여기 참고했음
@api_view(['POST'])
def dupicheck(request):
    if request.method == 'POST':
        serializer = DupiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            ImgUrl = serializer.data['dupiImg']

            dupiState = executeAImodel(ImgUrl)
            print(dupiState)
            return Response(dupiState, status=201) #원래는 serializer.data
        return Response(serializer.errors, status=400)
    #나중에 이 base64를 jpg로 변환한 후 코드에 돌리는 메서드를 만들어야함





