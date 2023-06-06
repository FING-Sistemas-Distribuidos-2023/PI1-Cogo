import os
import redis;
import ast

host = os.getenv('REDIS_HOST')
port = os.getenv('REDIS_PORT')

if(host == None or port == None):
    raise Exception("Invalid host or port (make sure you load REDIS_HOST and REDIS_PORT evironment variables")
else:
    r = redis.Redis(host=host,port=int(port), decode_responses=True)

queue = r.pubsub()
queue.subscribe("toBack")

def calculate(equation : str):
    try:
        ast_tree = ast.parse(equation, mode='eval')
        exp = compile(ast_tree, filename="<ast>", mode="eval")
        result = eval(exp)
    except:
        result = "ERROR"
    return result

while True:
    msg = queue.get_message(True) 
    if msg != None:
        result = calculate(str(msg['data']))
        r.publish("toFront",result) 