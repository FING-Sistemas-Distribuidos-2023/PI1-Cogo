from django.shortcuts import render
import os
import redis;

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

if(host == None or port == None):
    raise Exception("Invalid host or port (make sure you load REDIS_HOST and REDIS_PORT evironment variables")
else:
    r = redis.Redis(host=host,port=int(port), decode_responses=True)

sub = r.pubsub()
sub.subscribe('toFront')

def calchandler(request):
    if(request.method == "GET"):
        return render(request,'index.html',{'result':0});
    else:
        if(request.method == "POST"):
            num = request.number;
            r.publish("toFront",{'result' : num})
            msg = sub.get_message();
            while(msg!=None):
                for msg in sub.listen():
                    x = sub.get_message().get('num');
            return render(request,'index.html',{'result':int(x)});    