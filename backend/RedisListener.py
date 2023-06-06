import os
import redis;
import math;

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

if(host == None or port == None):
    raise Exception("Invalid host or port (make sure you load REDIS_HOST and REDIS_PORT evironment variables")
else:
    r = redis.Redis(host=host,port=int(port), decode_responses=True)

goQ = r.pubsub()
goQ.subscribe("toFront")
comeQ = r.pubsub()
comeQ.subscribe("toBack")

while True:    
    msg =  comeQ.get_message()
    if msg != None:
        print(msg)
        x = int(msg.get('data'))
        if(x != None):
            r.publish("toFront",x*x)    
        