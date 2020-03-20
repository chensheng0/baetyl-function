#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
function to say hi in python
"""

import json

def handler(event, context):
    resp = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {
	        "X-Custom-Header": "headerValue"
        },
        "body": "sss-xx"
    }
    return json.dumps(resp)