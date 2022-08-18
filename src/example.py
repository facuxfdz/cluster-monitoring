from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and request made
REQUEST_TIME = Summary('req_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request(t):
    """Dummy function that takes some time"""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(8006)
    # Generate some requests
    while True:
        process_request(random.random())