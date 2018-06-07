
def LoadXMLFromFile():
    fileName  = str(inpu("please input file name to load:"))
    global xmlFD

    try:
        xmlFD = open(fileName)
    except IOError:
        print("invalid file name or path")
        return None
    else:
        try:
            dom = parse(xnmFD)
        except Exception:
            print("loading fail")
        else:
            print("XML document loading complete")
            return dom
    return None

def MoviesFree():
    if checkDocument():
        response_body.unlink()

def PrintDOMtoXML():
    if checkDocument():
        print(response_body.toxml())







import http.client
import urllib.request

def search():

    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote("로맨스")

    conn.request("GET", "/v1/search/movie.json?movie&start=1&query="+encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    #
    req = conn.getresponse()
    print(req.status, req.reason)
    if int(req.status) == 200:
       response_body = req.read()
       print(response_body.decode('utf-8'))
    else:
     print("OpenAPI request has been failed!! please retry")

if __name__ == '__main__':
    print(search())



def SearchMovie():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote("로맨스")

    conn.request("GET", "/v1/search/movie.xml?movie&start=1&query=" + encText, None,
                    {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
        #
    req = conn.getresponse()

    print(req.status, req.reason)
    global DataList
    DataList.clear()

    if int(req.status) == 200:
        response_body = req.read()
        f = open(filename, "wb")
        f.write(response_body)
        f.close()

        tree = etree.parse(filename)
        root = tree.getroot()

        print(root.findall(''))
        for a in root.findall('.//item'):
            print("제목:", a.findtext('title'))
            print("링크:",a.findtext('link'))
            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('link'))
            print("데이터들어감")


    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, DataList[i][0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "링크 : ")
        RenderText.insert(INSERT, DataList[i][1])
        RenderText.insert(INSERT, "\n")

    print("끝")



def SearchMovie():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote("로맨스")

    conn.request("GET", "/v1/search/movie.xml?movie&start=1&query=" + encText, None,
                    {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
        #
    req = conn.getresponse()

    print(req.status, req.reason)
    global DataList
    DataList.clear()

    if int(req.status) == 200:
        response_body = req.read()
        f = open(filename, "wb")
        f.write(response_body)
        f.close()

        tree = etree.parse(filename)
        root = tree.getroot()

        print(root.findall(''))
        for a in root.findall('.//item'):
            print("제목:", a.findtext('title'))

        if response_body == None:
            print("에러")
        else:
            print("시작")
            parseData = parseString(filename)
            InfoMovie = parseData.childNodes
            row = InfoMovie[0].childNodes
            print(parseData)

            for item in row:
                print("들어감")
                #if item.nodeName=="title":
                    #print("더들어감")
                subitems = item.childNodes
                DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue,
                                     subitems[2].firstChild.nodeValue, subitems[3].firstChild.nodeValue,
                                 subitems[4].firstChild.nodeValue, subitems[5].firstChild.nodeValue,subitems[6].firstChild.nodeValue
                                 ),)

                print("데이터들어감")

    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "API : ")
        RenderText.insert(INSERT, a.findtext('title'))
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "주소 : ")
        RenderText.insert(INSERT, DataList[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "결과 : ")
        RenderText.insert(INSERT, DataList[i][2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "시간 : ")
        RenderText.insert(INSERT, DataList[i][3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, DataList[i][4])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, DataList[i][5])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, DataList[i][6])
        RenderText.insert(INSERT, "\n")

        RenderText.insert(INSERT, "\n")
        print("중간")
    print("끝")




 RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, DataList[8*i])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "링크 : ")
        RenderText.insert(INSERT, DataList[8*i+1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "이미지 : ")
        RenderText.insert(INSERT, DataList[8*i+2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "부제목 : ")
        RenderText.insert(INSERT, DataList[8*i+3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "년도 : ")
        RenderText.insert(INSERT, DataList[8*i+4])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "감독 : ")
        RenderText.insert(INSERT, DataList[8*i+5])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "배우 : ")
        RenderText.insert(INSERT, DataList[8*i+6])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "평점 : ")
        RenderText.insert(INSERT, DataList[8*i+7])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "\n")