from django.shortcuts import render

#REDIS
from redis import RedisCluster

rc = RedisCluster(host='localhost', port=16379)
sub = rc.pubsub()
sub.subscribe("toFront")

def sendToRedisQueue(i:int)->None:
    rc.publish("toBack",str(i))
    return ;
    
def readRedisQueue()->int:
    msg = sub.get_message()
    return int(msg['data'])

# Handlers
def sendValueHandler(request):
    sendToRedisQueue(request)
    x = readRedisQueue()
    return render(request,"index.html",{'result':x})
