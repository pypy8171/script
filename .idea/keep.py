
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


        ###########################3


def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=170, y=100)
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none', width=10, height=1, borderwidth=20, relief='ridge', yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(1, "영화 제목")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=100)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitSortListBox():
    global SortListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=120, y=240)
    TempFont = font.Font(window, size=12, weight='bold', family='Consolas')
    SortListBox = Listbox(window, font=TempFont, activestyle='none', width=8, height=1, borderwidth=10, relief='ridge', yscrollcommand=ListBoxScrollbar.set)
    SortListBox.insert(1, "제작년도")
    SortListBox.insert(2, "평점")
    SortListBox.pack()
    SortListBox.place(x=10, y=240)
    ListBoxScrollbar.config(command=SortListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=180)

def InitSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(window, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=190)

def SearchButtonAction():
    #global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    SearchMovie()
    RenderText.configure(state='disabled')


def InitSecondSearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SecondSearchButton = Button(window, font = TempFont, text="검색",  command=SecondSearchButtonAction)
    SecondSearchButton.pack()
    SecondSearchButton.place(x=150, y=250)


def SecondSearchButtonAction():
    global SecondSearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSecondSearchIndex = 0 #SearchListBox.curselection()[0]
    iSecondSearchIndex2 = 0
    if iSecondSearchIndex == 0:
        #SearchMovie()
        pass#sort() SearchMovie()
    elif iSearchIndex == 2:
        pass#SearchActor()

    RenderText.configure(state='disabled')

def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=15, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=5, y=300)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

def image():
    photo = PhotoImage(file="picture.gif")  # 디폴트 이미지 파일
    imageLabel = Label(window, image=photo)
    imageLabel.configure(image=photo)
    imageLabel.image = photo
    imageLabel.place(x=210,y=530)



def practice():
    def process():
        movie = (e1.get())
        e2.insert(0,movie)
        e2.search(0,movie)

    def reset():
        e2.delete(0,100)
        e1.delete(0,100)

    l1 = Label(window, text="검색란 ", font = 'helvetica 12 italic')
    l2 = Label(window, text="결과란", font = 'helvetica 12 italic')
    l1.place(x=40,y=250)
    l2.place(x=40,y=300)

    e1 = Entry(window)
    e2 = Entry(window)
    e1.place(x=130,y=250)
    e2.place(x=130,y=300)


    b1 = Button(window, text="검색",command=process)
    b1.grid(row=0,column=3); b1["bg"]="yellow"
    b1.place(x=300,y=250)

    b2 = Button(window, text="초기화",command=reset)
    b2.grid(row=1,column=3); b2["bg"]="yellow"
    b2.place(x=300,y=300)
