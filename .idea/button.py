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

window = Tk()
window.geometry("800x600+750+200")
DataList = []

##################################################################################################################################################################

def InitCountrySearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(window)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=570, y=100)
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none', width=10, height=1, borderwidth=20, relief='ridge', yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(1, "국가별 영화")
    SearchListBox.pack()
    SearchListBox.place(x=410, y=100)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitCountryInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=410, y=230)

def InitCountrySearchButton():
    global country
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton1 = Button(window, font = TempFont, text="한국",  command=CountrySearchButtonAction1)
    SearchButton2 = Button(window, font = TempFont, text="일본",  command=CountrySearchButtonAction2)
    SearchButton3 = Button(window, font = TempFont, text="미국",  command=CountrySearchButtonAction3)
    SearchButton4 = Button(window, font = TempFont, text="홍콩",  command=CountrySearchButtonAction4)
    SearchButton5 = Button(window, font = TempFont, text="프랑스",  command=CountrySearchButtonAction5)
    SearchButton6 = Button(window, font = TempFont, text="영국",  command=CountrySearchButtonAction6)
    SearchButton7 = Button(window, font = TempFont, text="기타",  command=CountrySearchButtonAction7)

    SearchButton1.pack()
    SearchButton1.place(x=410, y=190)
    SearchButton2.pack()
    SearchButton2.place(x=460, y=190)
    SearchButton3.pack()
    SearchButton3.place(x=510, y=190)
    SearchButton4.pack()
    SearchButton4.place(x=560, y=190)
    SearchButton5.pack()
    SearchButton5.place(x=605, y=190)
    SearchButton6.pack()
    SearchButton6.place(x=670, y=190)
    SearchButton7.pack()
    SearchButton7.place(x=720, y=190)


def CountrySearchButtonAction1():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction2():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    JP()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction3():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    US()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction4():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    HK()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction5():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    FR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction6():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    GB()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction7():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    ETC()
    RenderText.configure(state='disabled')


def InitCountryRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=775, y=200)
    TempFont = font.Font(window, size=10, family='Consolas')
    RenderText = Text(window, width=49, height=15, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=405, y=300)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')

def KR():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=KR&query=" + encText, None,
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
            print("제작년도",a.findtext('pubDate'))
            print("감독:",a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:",a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))



    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "제목 : ")
        RenderText.insert(INSERT, DataList[5*i])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "제작년도 : ")
        RenderText.insert(INSERT, DataList[5 * i+1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "감독 : ")
        RenderText.insert(INSERT, DataList[5 * i+2])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "배우 : ")
        RenderText.insert(INSERT, DataList[5*i+3])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i + 1)
        RenderText.insert(INSERT, "]")
        RenderText.insert(INSERT, "평점 : ")
        RenderText.insert(INSERT, DataList[5 * i + 4])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "\n")

def JP():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=JP&query=" + encText, None,
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
            # for j in range(0,30):
            print("제목:", a.findtext('title'))
            print("제작년도", a.findtext('pubDate'))
            print("감독:", a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:", a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제목 : ")
            RenderText.insert(INSERT, DataList[5 * i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제작년도 : ")
            RenderText.insert(INSERT, DataList[5 * i + 1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "감독 : ")
            RenderText.insert(INSERT, DataList[5 * i + 2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "배우 : ")
            RenderText.insert(INSERT, DataList[5 * i + 3])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "평점 : ")
            RenderText.insert(INSERT, DataList[5 * i + 4])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")

def US():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=US&query=" + encText, None,
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
            # for j in range(0,30):
            print("제목:", a.findtext('title'))
            print("제작년도", a.findtext('pubDate'))
            print("감독:", a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:", a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제목 : ")
            RenderText.insert(INSERT, DataList[5 * i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제작년도 : ")
            RenderText.insert(INSERT, DataList[5 * i + 1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "감독 : ")
            RenderText.insert(INSERT, DataList[5 * i + 2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "배우 : ")
            RenderText.insert(INSERT, DataList[5 * i + 3])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "평점 : ")
            RenderText.insert(INSERT, DataList[5 * i + 4])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")

def HK():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=HK&query=" + encText, None,
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
            # for j in range(0,30):
            print("제목:", a.findtext('title'))
            print("제작년도", a.findtext('pubDate'))
            print("감독:", a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:", a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제목 : ")
            RenderText.insert(INSERT, DataList[5 * i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제작년도 : ")
            RenderText.insert(INSERT, DataList[5 * i + 1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "감독 : ")
            RenderText.insert(INSERT, DataList[5 * i + 2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "배우 : ")
            RenderText.insert(INSERT, DataList[5 * i + 3])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "평점 : ")
            RenderText.insert(INSERT, DataList[5 * i + 4])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")


def FR():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=FR&query=" + encText, None,
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
            # for j in range(0,30):
            print("제목:", a.findtext('title'))
            print("제작년도", a.findtext('pubDate'))
            print("감독:", a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:", a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제목 : ")
            RenderText.insert(INSERT, DataList[5 * i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제작년도 : ")
            RenderText.insert(INSERT, DataList[5 * i + 1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "감독 : ")
            RenderText.insert(INSERT, DataList[5 * i + 2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "배우 : ")
            RenderText.insert(INSERT, DataList[5 * i + 3])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "평점 : ")
            RenderText.insert(INSERT, DataList[5 * i + 4])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")


def GB():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=GB&query=" + encText, None,
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
            # for j in range(0,30):
            print("제목:", a.findtext('title'))
            print("제작년도", a.findtext('pubDate'))
            print("감독:", a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:", a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제목 : ")
            RenderText.insert(INSERT, DataList[5 * i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제작년도 : ")
            RenderText.insert(INSERT, DataList[5 * i + 1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "감독 : ")
            RenderText.insert(INSERT, DataList[5 * i + 2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "배우 : ")
            RenderText.insert(INSERT, DataList[5 * i + 3])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "평점 : ")
            RenderText.insert(INSERT, DataList[5 * i + 4])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")


def ETC():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=ETC&query=" + encText, None,
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
            # for j in range(0,30):
            print("제목:", a.findtext('title'))
            print("제작년도", a.findtext('pubDate'))
            print("감독:", a.findtext('director'))
            print("배우:", a.findtext('actor'))
            print("평점:", a.findtext('userRating'))

            DataList.append(a.findtext('title'))
            DataList.append(a.findtext('pubDate'))
            DataList.append(a.findtext('director'))
            DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제목 : ")
            RenderText.insert(INSERT, DataList[5 * i])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제작년도 : ")
            RenderText.insert(INSERT, DataList[5 * i + 1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "감독 : ")
            RenderText.insert(INSERT, DataList[5 * i + 2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "배우 : ")
            RenderText.insert(INSERT, DataList[5 * i + 3])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "평점 : ")
            RenderText.insert(INSERT, DataList[5 * i + 4])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")




##########################################################################################################################################

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="[영화 검색 App]")
    MainText.place(x=290,y=20)

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
    global SearchListBox
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    iSearchIndex = 0
    if iSearchIndex == 0:
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

def SearchMovie():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&&query=" + encText, None,
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

#practice()
InitRenderText()
InitCountryRenderText()
InitTopText()
InitSearchListBox()
InitCountrySearchListBox()
InitInputLabel()
InitCountryInputLabel()
InitCountrySearchButton()
InitSearchButton()
InitSecondSearchButton()
InitSortListBox()
image()
window.mainloop()
