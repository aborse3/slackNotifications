import requests
import json


def handler_name(event,context):
    print (event)
    SlackMessage={'text': str(event)}
    r=requests.post('https://hooks.slack.com/services/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',data=json.dumps(SlackMessage))
    print(r.status_code, r.reason)
    return r.status_code
