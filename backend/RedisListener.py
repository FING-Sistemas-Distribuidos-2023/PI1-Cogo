import os
import redis;
import math;

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

if(host == None or port == None):
    raise Exception("Invalid host or port (make sure you load REDIS_HOST and REDIS_PORT evironment variables")
else:
    r = redis.Redis(host=host,port=int(port), decode_responses=True)

sub = r.pubsub()
sub.subscribe("toBack")

while True:
    for msg in sub.listen():
        if msg != None:
            x = msg.get('num');
            if(x!= None):
                i = x*x;
                r.publish("toFront",{'result' : x})