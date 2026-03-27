import requests
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzc0NjIzNjQyfQ.kKHBHat8ztBY4TeOmtczi9z4ao0V04-EE-jcNkSTQtc"
}
req = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(req)
print(req.json())