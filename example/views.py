from django.shortcuts import render
from .tasks import add, summ
from django.http import HttpResponse

# Create your views here.
def task_state(request):
    result = summ.delay(4,8)
    return HttpResponse(str(result.task_id)+"/"+str(result.status)+"/"+str(result.id))
    

from celery.result import AsyncResult

def redisResult(request):
    idd = request.GET.get('id')
    res = AsyncResult(idd,app=add)
    return HttpResponse("/"+str(res.status)+"/"+str(res.state)+"/"+str(res.ready()))
