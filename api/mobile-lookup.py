import requests
from urllib.parse import urlencode
from flask import jsonify

def handler(request):
    key = request.args.get("key")
    mobile = request.args.get("mobile")

    if not key or not mobile:
        return jsonify({
            "success": False,
            "message": "key and mobile are required"
        }), 400

    # 🔥 ORIGINAL API WITH PORT 10000
    target_url = "http://149.102.129.108:10000/mobile-lookup"

    query = urlencode({
        "key": key,
        "mobile": mobile
    })

    resp = requests.get(f"{target_url}?{query}", timeout=15)

    # ✅ RETURN SAME JSON (NO CHANGE)
    return jsonify(resp.json()), resp.status_code
