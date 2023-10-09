from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .flattener import flattenJsonFunc
from .models import FlattenedJsonModel
from .serializer import FlattenedJsonSerializer

class JsonFlattenerViewSet(APIView):
    def post(self, request, format=None):
        inputJson = request.data

        if not inputJson:
            return Response({'Error': 'Input JSON is required'}, status=status.HTTP_400_BAD_REQUEST)

        flattenedJson = {}
        flattenJsonFunc(inputJson,flattenedJson)

        jsonData = FlattenedJsonModel(inputJson=inputJson, flattenedJson=flattenedJson)
        jsonData.save()
        
        serializer = FlattenedJsonSerializer(jsonData)
        return Response(serializer.data['flattenedJson'], status=status.HTTP_201_CREATED)
    
    def get(self, request, format=None):
        flattenedData = FlattenedJsonModel.objects.all()
        serializer = FlattenedJsonSerializer(flattenedData, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
