import http.client
import urllib.request

server = "openapi.naver.com"
client_id = "YoEm7X7SqpQXmWrqJHKn"
client_secret = "MgMAZsI63y"
conn = http.client.HTTPSConnection(server)

encText = urllib.parse.quote("공포")

conn.request("GET", "/v1/search/movie.xml?genre=10&start=1&query="+encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})

req = conn.getresponse()
print(req.status, req.reason)
if int(req.status) == 200:
    response_body = req.read()
    print(response_body.decode('utf-8'))
else:
    print("OpenAPI request has been failed!! please retry")