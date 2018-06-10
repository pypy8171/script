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
    ListBoxScrollbar.place(x=170, y=100)
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(window, font=TempFont, activestyle='none', width=10, height=1, borderwidth=20, relief='ridge', yscrollcommand=ListBoxScrollbar.set)
    SearchListBox.insert(1, "영화 검색")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=100)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitCountryInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=5, y=190)

def InitCountrySearchButton():
    global country
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(window, font = TempFont, text="검색",  command=CountrySearchButtonAction)
    SearchButton1 = Button(window, font = TempFont, text="한국",  command=CountrySearchButtonAction1)
    SearchButton2 = Button(window, font = TempFont, text="일본",  command=CountrySearchButtonAction2)
    SearchButton3 = Button(window, font = TempFont, text="미국",  command=CountrySearchButtonAction3)
    SearchButton4 = Button(window, font = TempFont, text="홍콩",  command=CountrySearchButtonAction4)
    SearchButton5 = Button(window, font = TempFont, text="프랑스",  command=CountrySearchButtonAction5)
    SearchButton6 = Button(window, font = TempFont, text="영국",  command=CountrySearchButtonAction6)
    SearchButton7 = Button(window, font = TempFont, text="기타",  command=CountrySearchButtonAction7)

    SearchButton.pack()
    SearchButton.place(x=320, y=200)
    SearchButton1.pack()
    SearchButton1.place(x=10, y=250)
    SearchButton2.pack()
    SearchButton2.place(x=60, y=250)
    SearchButton3.pack()
    SearchButton3.place(x=110, y=250)
    SearchButton4.pack()
    SearchButton4.place(x=160, y=250)
    SearchButton5.pack()
    SearchButton5.place(x=205, y=250)
    SearchButton6.pack()
    SearchButton6.place(x=270, y=250)
    SearchButton7.pack()
    SearchButton7.place(x=320, y=250)

def CountrySearchButtonAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    SearchMovie()
    RenderText.configure(state='disabled')

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
    RenderText.place(x=5, y=300)
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
        RenderText.insert(INSERT, "< 한국 영화 >")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "\n")
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
            RenderText.insert(INSERT, "< 일본 영화 >")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
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
            RenderText.insert(INSERT, "< 미국 영화 >")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
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
            RenderText.insert(INSERT, "< 홍콩 영화 >")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
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
            RenderText.insert(INSERT, "< 프랑스 영화 >")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
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
            RenderText.insert(INSERT, "< 영국 영화 >")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
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
            RenderText.insert(INSERT, "< 기타 >")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
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
        RenderText.insert(INSERT, "< 전체 >")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "\n")
                # for j in range(0, 7):
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


##########################################################################################################################################

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="[영화 검색 App]")
    MainText.place(x=290,y=20)


def image():
    photo = PhotoImage(file="picture.gif")  # 디폴트 이미지 파일
    imageLabel = Label(window, image=photo)
    imageLabel.configure(image=photo)
    imageLabel.image = photo
    imageLabel.place(x=210,y=530)


#practice()
#InitRenderText()
InitCountryRenderText()
InitTopText()
#InitSearchListBox()
InitCountrySearchListBox()
#InitInputLabel()
InitCountryInputLabel()
#InitSearchButton()
InitCountrySearchButton()
#InitSecondSearchButton()
#InitSortListBox()
image()
window.mainloop()
