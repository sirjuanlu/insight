#!/bin/env python

import requests
import json
import hashlib
import base64
import time
import hmac
import datetime
from datetime import timedelta

#Account Info
AccessId =''
AccessKey =''
Company = ''
WidgetId =

#Request Info
httpVerb ='GET'
resourcePath = '/dashboard/widgets/{}/data'.format(WidgetId)

#Get current time in milliseconds
epoch = str(int(time.time() * 1000))
earlier = str(int((datetime.datetime.now() - datetime.timedelta(minutes=60)).timestamp()))
queryParams ='?start='+earlier+'&end='+epoch

#Construct URL 
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath + queryParams

#Concatenate Request details
requestVars = httpVerb + epoch + resourcePath


#Construct signature
#hmac1 = hmac.new(AccessKey.encode(),msg=requestVars.encode(),digestmod=hashlib.sha256).hexdigest()
signature = base64.b64encode(hmac.new(bytes(AccessKey, 'utf-8'),msg=bytes(requestVars, 'utf-8'),digestmod=hashlib.sha256).hexdigest().encode())


#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature.decode() + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth}

#Make request
response = requests.get(url, headers=headers)

#Print status and body of response
print('Response Status:',response.status_code)
# print('Response Body:',response.content)

# Graph Info
GraphTitle = ""
VerticalLabel = ""
Series = []
Timestamp = []

if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
    dd = data["data"]
    GraphTitle = dd["title"]
    VerticalLabel = dd["verticalLabel"]
    Timestamp = dd["timestamps"]
    print(dd)
    # print(Timestamp)

    for line in dd["lines"]:
        serie = {
                "name" : line["legend"],
                "color": line["color"],
                "data": line["data"]
            }
        Series.append(serie)
        # print(serie)
    print(Series)
else:
    print("ERROR request, status %d",response.status_code)

##### Insight code ####
#Sample code for a graph widget

# def get(event, context):
#     return {
#         "type": "graph",
#         "version": 0.2,
#         "config": {
#             "chart": {
#                 "type": "column"
#             },
#             "title": {
#                 "text": GraphTitle
#             },
#             "yAxis": {
#                 "min": 0,
#                 "title": {
#                     "text": None
#                 }
#             },
#             "xAxis": {
#                 "categories": Timestamp,
#                 "title": {
#                     "text": "Timestamp",
#                     "align": "high"
#                 }
#             },
#             "series": Series
#         }
#     }