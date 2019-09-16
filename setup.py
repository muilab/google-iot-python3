# -*- coding: utf-8 -*-

import os

GOOGLE_IOT_SERVICE_JSON = os.environ.get('GOOGLE_IOT_SERVICE_JSON')

service_json = '/data/service.json'
with open(service_json, 'w') as f:
    dst = GOOGLE_IOT_SERVICE_JSON.replace("'", "\"")
    f.write(dst)
    f.close()


