import requests
import json
webhook_url = 'https://webhook.site/4fed7efb-57c9-4571-9b4a-66097a849cd9'

data = { 'name': 'MAINrepo', 
         'Channel URL': 'https://github.com/Anjana-msnaico/MAINRepo.git' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})