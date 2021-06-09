import prometheus_client as prom
from prometheus_client import Gauge , REGISTRY
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
import random
import time
import requests


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        me_username = "$USERNAME"
        me_password = "$PASSWORD"
        me_token = "$TOKEN"
        payload = {'grant_type': 'password','username': $me_username,'password': $me_password}
        headers = {'Host': 'x.x.x.x','Content-Type': 'application/json', } # if use header for your requst
        #another api auth
        you_auth = '{ "username": "$USERNAME", "password": "$PASSWORD" }'

        # this is sample api call with token for me api
        me_api_request = requests.post('http://$API/token', verify=False, headers={'Authorization':"Basic %s" % metoken , "Content-Type":"application/x-www-form-urlencoded"}, data=payload)
        
        #this is sample api call with user pass for you api
        you_api_request = requests.post('http://IP:PORT/API', headers=headers, data=youauth)

        g_me_api_request = GaugeMetricFamily("response_time", 'Help text', labels=['time'])
        g_me_api_request.add_metric(["me_api_request.time"], me_api_request.elapsed.total_seconds())
        yield g_me_api_request

        c_me_api_request = CounterMetricFamily("status_code", 'Help text', labels=['url'])
        print (me_api_request.status_code)
        c_me_api_request.add_metric(["me_api_request.status.code"],me_api_request.status_code )
        yield c_me_api_request


        g_you_api_request = GaugeMetricFamily("response_time", 'Help text', labels=['time'])
        g_you_api_request.add_metric(["you_api_request.time"], you_api_request.elapsed.total_seconds())
        yield g_you_api_request

        c_you_api_request = CounterMetricFamily("status_code", 'Help text', labels=['url'])
        print (you_api_request.status_code)
        c_you_api_request.add_metric(["you_api_request.status.code"],you_api_request.status_code )
        yield c_you_api_request

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    prom.start_http_server(3010)
    REGISTRY.register(CustomCollector())
    # Generate some requests.
    while True:

        time.sleep(1)
