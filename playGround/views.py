from datetime import datetime, timedelta

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import models
from rest_framework import status
from .models import ShowCase

# Create your views here.

@api_view(['GET'])
def get_show_cases(request):
    try:
        skip = int(request.query_params.get('skip', 0))
        limit = int(request.query_params.get('limit', 10))

        show_cases = ShowCase.objects.all()[skip:skip + limit]
        
        # Serialize the data
        show_cases_list = []
        for show_case in show_cases:
            show_cases_list.append({
                'url': show_case.url,
                'likeCount': show_case.likeCount,
                'commentCount': show_case.commentCount,
            })
        data = {
            "showCases": show_cases_list
        }

        response_data = {
            "code": 200,
            "msg": "Success",
            "data": data
        }

        return Response(response_data, status=status.HTTP_200_OK)
    except ValueError:
        return Response({'error': 'Invalid skip or limit parameter'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

