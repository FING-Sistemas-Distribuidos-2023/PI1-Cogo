from django.shortcuts import render
from django.http import HttpResponse

#REDIS
from redis import RedisCluster

rc = RedisCluster(host='localhost', port=16379)
sub = rc.pubsub()
sub.subscribe("toBack")

def sendToRedisQueue(i:int)->None:
    rc.publish("toFront",str(i))
    return ;
    
def readRedisQueue()->int:
    msg = sub.get_message()
    r = int(msg['data'])
    return r*r;

# Create your views here.

def addkeyValueHandler(request):
        request
    return HttpResponse('Se añadio el valor 1');
