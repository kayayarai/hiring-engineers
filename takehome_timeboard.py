# Utilize the Datadog API to create a Timeboard that contains:
#    my_metric scoped over your host.
#    Any metric from the Integration on your Database with the anomaly function applied.
# 
from datadog import initialize, api

options = {'api_key': 'redacted',
           'app_key': 'redacted',
           'api_host': 'https://api.datadoghq.com'}

initialize(**options)

title = 'Dashboard for Takehome'
widgets = [{
    'definition': {
        'type': 'timeseries',
        'requests': [
        {
            "q": "avg:my_metric{host:vagrant}",
        }
    ],
        'title': 'Random chosen number over time'
    }
},
    {'definition': {
        'type': 'timeseries',
        'requests': [
        {

            "q": "anomalies(avg:mongodb.tcmalloc.tcmalloc.central_cache_free_bytes{host:vagrant}, 'basic', 2, direction='below')",
        }
    ],
        'title': 'Free central cache (bytes)'
    }
    }
]
layout_type = 'ordered'
description = 'This is a dashboard made by Kari in answer to a takehome test.'
is_read_only = True
notify_list = ['kari.halsted.ca@gmail.com']

api.Dashboard.create(title=title,
                     widgets=widgets,
                     layout_type=layout_type,
                     description=description,
                     is_read_only=is_read_only,
                     notify_list=notify_list)
