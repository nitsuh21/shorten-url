from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import URLMapping
from .serializers import URLMappingSerializer
import string
import random

@api_view(['POST'])
def shorten_url(request):
    print('method')
    if request.method == 'POST':
        original_url = request.data.get('original_url')
        if original_url:
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            url_mapping = URLMapping(original_url=original_url, short_url=short_url)
            url_mapping.save()
            serializer = URLMappingSerializer(url_mapping)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Missing original_url parameter'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def access_url(request, short_url):
    try:
        url_mapping = URLMapping.objects.get(short_url=short_url)
    except URLMapping.DoesNotExist:
        return Response({'error': 'Short URL not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = URLMappingSerializer(url_mapping)
        return Response(serializer.data)
