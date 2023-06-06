from django.shortcuts import render
from django.http import request, response
from django import forms

import os
import redis;


host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

if(host == None or port == None):
    raise Exception("Invalid host or port (make sure you load REDIS_HOST and REDIS_PORT evironment variables")
else:
    r = redis.Redis(host=host,port=int(port), decode_responses=True)

goQ = r.pubsub()
goQ.subscribe("toBack")
comeQ = r.pubsub()
comeQ.subscribe("toFront")

def getHandler(request : request)->response:
    opResult : int = 0;
    if(request.method == "POST"):
        a = request.POST.get("number")
        r.publish("toBack",int(a));
        msg = None
        while msg == None:
            msg = comeQ.get_message();
            if(msg!=None):
                opResult = int(msg.get('data'));
    return render(request,'index.html',{'result':opResult});