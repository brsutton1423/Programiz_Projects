from openai import OpenAI
import requests as r

response = r.get("https://api.openai.com/v1/organization/admin_api_keys")
print(response.json())