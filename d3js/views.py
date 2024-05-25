from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from .models import VisitCount
from django.db.models import Count
from datetime import datetime, timedelta

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def say_hello(request):
    return Response("Hello World!!")



# 记录访问的视图
@api_view(['GET'])
def record_visit(request):
    ip_address = request.META.get('REMOTE_ADDR')
    VisitCount.objects.create(ip_address=ip_address)
    return JsonResponse({"message": "Visit recorded"})

@api_view(['GET'])
def recent_visit_count(request):
    # 获取十天前的日期
    ten_days_ago = datetime.now().date() - timedelta(days=10)

    # 获取过去十天的访问量统计
    recent_visits = VisitCount.objects.filter(happen_time__date__gte=ten_days_ago) \
                                       .values('happen_time__date') \
                                       .annotate(visit_count=Count('id'))

    # 格式化数据
    data = [{"date": visit['happen_time__date'], "visit_count": visit['visit_count']} for visit in recent_visits]

    return Response(data)

