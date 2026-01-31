import requests
from urllib.parse import urlencode

def handler(request):
    params = request.args

    key = params.get("key")
    mobile = params.get("mobile")

    if not key or not mobile:
        return {
            "statusCode": 400,
            "body": {
                "success": False,
                "message": "key and mobile are required"
            }
        }

    target_url = "http://149.102.129.108:10000/mobile-lookup"

    query = urlencode({
        "key": key,
        "mobile": mobile
    })

    response = requests.get(f"{target_url}?{query}", timeout=10)

    return {
        "statusCode": response.status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": response.json()
    }
