# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:18:46 2020

@author: walia
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())