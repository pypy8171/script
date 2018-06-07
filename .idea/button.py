import sys
from tkinter import*
from tkinter import font
import tkinter.messagebox
import Movie
import http.client
import urllib.request
import urllib.parse
import xml.etree.ElementTree as etree
from xml.dom.minidom import parse, parseString
import xml.dom.minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import parse
import json

filename = 'movie.xml'

loopFlag =1
xmlFD = -1
response_body = None

#import json
#from collections import OrderedDict
#from pprint import pprint

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

#rendertext 만들어야됨
def SearchButtonAction():
    global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = 0
    iSearchIndex2 = 0
    if iSearchIndex == 0:
        SearchMovie()
    if iSearchIndex ==1:
        Sort()
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
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

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
            #for j in range(0,30):
            print("제목:", a.findtext('title'))
            print("링크:", a.findtext('link'))
            print("이미지:", a.findtext('image'))
            print("부제:", a.findtext('subtitle'))
            print("년도:", a.findtext('pubDate'))
            print("감독:", a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:", a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('link'))
            DataList.append(a.findtext('image'))
            DataList.append(a.findtext('subtitle'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))


    for i in range(len(DataList)):
       #for j in range(0, 7):
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, DataList[8 * i])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "링크 : ")
        RenderText.insert(INSERT, DataList[8 * i + 1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "이미지 : ")
        RenderText.insert(INSERT, DataList[8 * i + 2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "부제목 : ")
        RenderText.insert(INSERT, DataList[8 * i + 3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "년도 : ")
        RenderText.insert(INSERT, DataList[8 * i + 4])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "감독 : ")
        RenderText.insert(INSERT, DataList[8 * i + 5])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "배우 : ")
        RenderText.insert(INSERT, DataList[8 * i + 6])
        RenderText.insert(INSERT, "\n")
    if DataList[8 + i + 7] < DataList[8 + (i + 1) + 7]:
        DataList[8 + i + 7], DataList[8 + (i + 1) + 7] = DataList[8 + (i + 1) + 7], DataList[8 + i + 7]
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "평점 : ")
        RenderText.insert(INSERT, DataList[8 * i + 7])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "\n")





def image():
    photo = PhotoImage(file="picture.gif")  # 디폴트 이미지 파일
    imageLabel = Label(window, image=photo)
    imageLabel.configure(image=photo)
    imageLabel.image = photo
    imageLabel.place(x=10,y=530)



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
image()
window.mainloop()
