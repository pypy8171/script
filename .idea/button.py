from tkinter import*
from tkinter import font
import tkinter.messagebox
import Movie


#def change_img():
#    path = inputBox.get()
#    img = PhotoImage(file = path)
#    imageLabel.configure(image = img)
#    imageLabel.image = img

#photo = PhotoImage(file="5.png")  # 디폴트 이미지 파일
#imageLabel = Label(window, image=photo)
#imageLabel.pack()
#inputBox = Entry(window)
#inputBox.pack()
#button = Button(window, text='클릭', command=change_img)
#button.pack()

window = Tk()
window.geometry("400x600+750+200")
DataList = []

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="[영화 검색 App]")
    MainText.place(x=90,y=20)

def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=170, y=100)
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none', width=10, height=1, borderwidth=20, relief='ridge', yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(1, "영화 제목")
    SearchListBox.insert(2, "영화 장르")
    SearchListBox.insert(3, "배우 이름")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=100)

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

#rendertext 만들어야됨
def SearchButtonAction():
    global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = 0
    if iSearchIndex == 0:
        SearchMovie()
    elif iSearchIndex == 1:
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()
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

def SearchMovie():
    import http.client
    import urllib.request
    from xml.dom.minidom import parse, parseString
    # conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    # conn.request("GET","/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    # req = conn.getresponse()
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote("로맨스")

    conn.request("GET", "/v1/search/movie.xml?movie&start=1&query=" + encText, None, {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    #
    req = conn.getresponse()
    print(req.status, req.reason)

    global DataList
    DataList.clear()
    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            print("됨")
            parseData = parseString(BooksDoc)
            GeoInfoLibrary = parseData.childNodes
            row = GeoInfoLibrary[0].childNodes
            for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
                    if subitems[0].firstChild.nodeValue == InputLabel.get():
                        pass
                    elif subitems[1].firstChild.nodeValue == InputLabel.get():
                        pass
                    if subitems[2].firstChlld is not None:
                        name = str(subitems[2].firstChild.nodeValue)
                        pass
                        DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, name))
                    else:
                        DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, "-"))
            print("된")
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
                RenderText.insert(INSERT, "[")
                RenderText.insert(INSERT, i + 1)
                RenderText.insert(INSERT, "]")
                RenderText.insert(INSERT, "tel : ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")


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

#practice()
InitRenderText()
InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()

InitSortListBox()
#change_img()
window.mainloop()
