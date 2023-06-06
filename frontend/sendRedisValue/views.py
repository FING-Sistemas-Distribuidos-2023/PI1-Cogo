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

queue = r.pubsub()
queue.subscribe("toFront")
queue.get_message()

def getHandler(request : request)->response:
    opResult : int = 0;
    if(request.method == "POST"):
        a = request.POST.get("number")
        r.publish("toBack",int(a));
        msg = None
        while msg == None:
            msg = queue.get_message();
            if(msg!=None):
                opResult = int(msg.get('data'));
    return render(request,'index.html',{'result':opResult});

def calculatorHandler(request : request)->response:
    result = "";
    if(request.method == "POST"):
        r.publish("toBack",request.POST.get("Screen"));
        msg = None
        while(msg == None):
            msg = queue.get_message(True)
            if(msg != None):
                result = msg.get('data');
    return render(request,'calculator.html',{'result':result});