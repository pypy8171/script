import http.client
import xml.etree.ElementTree as etree
import urllib.parse
import urllib.request

filename = 'movie.xml'

def search():

    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote("로맨스")

    conn.request("GET", "/v1/search/movie.xml?movie&start=1&query="+encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    #




    req = conn.getresponse()
    print(req.status, req.reason)

    if int(req.status) == 200:
       response_body = req.read()
       f = open(filename, "wb")
       f.write(response_body)
       f.close()
       #print(response_body.decode('utf-8'))

       tree = etree.parse(filename)
       root = tree.getroot()

       print(root.findall(''))
       for a in root.findall('.//item'):
           print("제목:",a.findtext('title'))

    else:
     print("OpenAPI request has been failed!! please retry")

if __name__ == '__main__':
    print(search())