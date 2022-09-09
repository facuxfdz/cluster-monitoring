from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary,Counter,Histogram,Gauge
import random
import time

app = Flask(__name__)

_INF = float("inf")

# We're going to define our metrics here
graphs = {}
graphs['c'] = Counter('python_request_operations_total','The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds', buckets=(0.2,0.5,0.7,1,2,_INF))

@app.route("/")
def hello():
    start = time.time()
    graphs['c'].inc()

    time.sleep(random.uniform(0.5,2))
    end = time.time()
    graphs['h'].observe(end-start)
    return f"""
    Hi! 
    Your request duration time: {end-start}
    See u later :)
    """

@app.route("/metrics")
def requests_count():
    res = []
    for k,v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res,mimetype="text/plain")
