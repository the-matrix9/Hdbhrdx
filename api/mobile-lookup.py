import requests
import json
from urllib.parse import urlencode
from http.server import BaseHTTPRequestHandler

def handler(request):
    key = request.args.get("key")
    mobile = request.args.get("mobile")

    if not key or not mobile:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "success": False,
                "message": "key and mobile are required"
            })
        }

    target_url = "http://149.102.129.108:10000/mobile-lookup"
    query = urlencode({"key": key, "mobile": mobile})

    resp = requests.get(f"{target_url}?{query}", timeout=15)

    # 🔥 VERY IMPORTANT: json.dumps
    return {
        "statusCode": resp.status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(resp.json())
    }
