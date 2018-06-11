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
window.geometry("600x600+750+200")
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
    SearchListBox.place(x=100, y=100)
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitCountryInputLabel():
    global InputLabel
    TempFont = font.Font(window, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(window, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=5, y=190)

def InitCountrySearchButton():
    TempFont = font.Font(window, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(window, font = TempFont, text="검색",  command=CountrySearchButtonAction)
    SearchButton1 = Button(window, font = TempFont, text="한국",  command=CountrySearchButtonAction1)
    SearchButton2 = Button(window, font = TempFont, text="일본",  command=CountrySearchButtonAction2)
    SearchButton3 = Button(window, font = TempFont, text="미국",  command=CountrySearchButtonAction3)
    SearchButton4 = Button(window, font = TempFont, text="홍콩",  command=CountrySearchButtonAction4)
    SearchButton5 = Button(window, font = TempFont, text="프랑스",  command=CountrySearchButtonAction5)
    SearchButton6 = Button(window, font = TempFont, text="영국",  command=CountrySearchButtonAction6)
    SearchButton7 = Button(window, font = TempFont, text="기타",  command=CountrySearchButtonAction7)
    SearchButton8 = Button(window, font=TempFont, text="10점", command=CountrySearchButtonAction8)
    SearchButton9 = Button(window, font=TempFont, text="9점", command=CountrySearchButtonAction9)
    SearchButton10 = Button(window, font=TempFont, text="8점", command=CountrySearchButtonAction10)
    SearchButton11 = Button(window, font=TempFont, text="7점", command=CountrySearchButtonAction11)
    SearchButton12 = Button(window, font=TempFont, text="6점", command=CountrySearchButtonAction12)
    SearchButton13 = Button(window, font=TempFont, text="5점", command=CountrySearchButtonAction13)
    SearchButton14 = Button(window, font=TempFont, text="4점", command=CountrySearchButtonAction14)
    SearchButton15 = Button(window, font=TempFont, text="3점", command=CountrySearchButtonAction15)
    SearchButton16 = Button(window, font=TempFont, text="2점", command=CountrySearchButtonAction16)
    SearchButton17 = Button(window, font=TempFont, text="1점", command=CountrySearchButtonAction17)
    SearchButton18 = Button(window, font=TempFont, text="0점", command=CountrySearchButtonAction18)
    SearchButton19 = Button(window, font=TempFont, text="2010~2018년", command=CountrySearchButtonAction19)
    SearchButton20 = Button(window, font=TempFont, text="2000~2009년", command=CountrySearchButtonAction20)
    SearchButton21 = Button(window, font=TempFont, text="1990~1999년", command=CountrySearchButtonAction21)
    SearchButton22 = Button(window, font=TempFont, text="1980~1989년", command=CountrySearchButtonAction22)
    SearchButton23 = Button(window, font=TempFont, text="1970~1979년", command=CountrySearchButtonAction23)
    SearchButton24 = Button(window, font=TempFont, text="1960~1969년", command=CountrySearchButtonAction24)
    SearchButton25 = Button(window, font=TempFont, text="1950~1959년", command=CountrySearchButtonAction25)
    SearchButton26 = Button(window, font=TempFont, text="1940~1949년", command=CountrySearchButtonAction26)
    SearchButton27 = Button(window, font=TempFont, text="1930~1939년", command=CountrySearchButtonAction27)
    SearchButton28 = Button(window, font=TempFont, text="1920~1929년", command=CountrySearchButtonAction28)

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
    SearchButton8.pack()
    SearchButton8.place(x=420, y=90)
    SearchButton9.pack()
    SearchButton9.place(x=420, y=130)
    SearchButton10.pack()
    SearchButton10.place(x=420, y=170)
    SearchButton11.pack()
    SearchButton11.place(x=420, y=210)
    SearchButton12.pack()
    SearchButton12.place(x=420, y=250)
    SearchButton13.pack()
    SearchButton13.place(x=420, y=290)
    SearchButton14.pack()
    SearchButton14.place(x=420, y=330)
    SearchButton15.pack()
    SearchButton15.place(x=420, y=370)
    SearchButton16.pack()
    SearchButton16.place(x=420, y=410)
    SearchButton17.pack()
    SearchButton17.place(x=420, y=450)
    SearchButton18.pack()
    SearchButton18.place(x=420, y=490)
    SearchButton19.pack()
    SearchButton19.place(x=470, y=90)
    SearchButton20.pack()
    SearchButton20.place(x=470, y=130)
    SearchButton21.pack()
    SearchButton21.place(x=470, y=170)
    SearchButton22.pack()
    SearchButton22.place(x=470, y=210)
    SearchButton23.pack()
    SearchButton23.place(x=470, y=250)
    SearchButton24.pack()
    SearchButton24.place(x=470, y=290)
    SearchButton25.pack()
    SearchButton25.place(x=470, y=330)
    SearchButton26.pack()
    SearchButton26.place(x=470, y=370)
    SearchButton27.pack()
    SearchButton27.place(x=470, y=410)
    SearchButton28.pack()
    SearchButton28.place(x=470, y=450)

def CountrySearchButtonAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    SearchMovie()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction1():
    global country
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    country =1
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction2():
    global country
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    country =2
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction3():
    global country
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    country=3
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction4():
    global country
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    country=4
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction5():
    global country
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    country=5
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction6():
    global country
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    country=6
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction7():
    global country
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    country=7
    KR()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction8():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num=10
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction9():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 9
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction10():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 8
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction11():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 7
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction12():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 6
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction13():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 5
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction14():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 4
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction15():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 3
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction16():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 2
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction17():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 1
    Rating5()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction18():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 0
    Rating5()
    RenderText.configure(state='disabled')


def CountrySearchButtonAction19():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 11
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction20():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 12
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction21():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 13
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction22():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 14
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction23():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 15
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction24():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 16
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction25():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 17
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction26():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 18
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction27():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 19
    SearchYear()
    RenderText.configure(state='disabled')

def CountrySearchButtonAction28():
    global num
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    num = 20
    SearchYear()
    RenderText.configure(state='disabled')


def InitCountryRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=475, y=200)
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

    if country ==1:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=KR&query=" + encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif country == 2:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=JP&query=" + encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif country == 3:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=US&query=" + encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif country == 4:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=HK&query=" + encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif country == 5:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=FR&query=" + encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif country == 6:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=GB&query=" + encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif country == 7:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&country=ETC&query=" + encText, None,{"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})

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

    #RenderText.insert(INSERT, "< 한국 영화 >")
    if country==1:
        RenderText.insert(INSERT, "< 한국 영화 >")
    elif country==2:
        RenderText.insert(INSERT, "< 일본 영화 >")
    elif country==3:
        RenderText.insert(INSERT, "< 미국 영화 >")
    elif country==4:
        RenderText.insert(INSERT, "< 중국 영화 >")
    elif country==5:
        RenderText.insert(INSERT, "< 프랑스 영화 >")
    elif country==6:
        RenderText.insert(INSERT, "< 영국 영화 >")
    elif country==7:
        RenderText.insert(INSERT, "< 기타 >")
    for i in range(len(DataList)):
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

    RenderText.insert(INSERT, "< 전체 >")
    for i in range(len(DataList)):
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "[")
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

def Rating5():
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
            DataList.append(a.findtext('title'))
            #DataList.append(a.findtext('pubDate'))
            #DataList.append(a.findtext('director'))
            #DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

    if num ==10:
        RenderText.insert(INSERT,  "< 평점 10인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='10.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==9:
        RenderText.insert(INSERT,  "< 평점 9인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='9.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==8:
        RenderText.insert(INSERT,  "< 평점 8인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='8.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==7:
        RenderText.insert(INSERT,  "< 평점 7인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='7.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==6:
        RenderText.insert(INSERT,  "< 평점 6인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='6.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==5:
        RenderText.insert(INSERT,  "< 평점 5인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='5.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==4:
        RenderText.insert(INSERT,  "< 평점 4인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='4.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==3:
        RenderText.insert(INSERT,  "< 평점 3인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='3.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==2:
        RenderText.insert(INSERT,  "< 평점 2인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='2.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==1:
        RenderText.insert(INSERT,  "< 평점 1인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='1.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

    elif num ==0:
        RenderText.insert(INSERT,  "< 평점 0인 영화 > ")
        RenderText.insert(INSERT, "\n")
        for i in range(len(DataList)):
            if DataList[i]=='0.00':
                RenderText.insert(INSERT, "제목 : ")
                RenderText.insert(INSERT, DataList[i-1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "\n")

def SearchYear():
    server = "openapi.naver.com"
    client_id = "YoEm7X7SqpQXmWrqJHKn"
    client_secret = "MgMAZsI63y"
    conn = http.client.HTTPSConnection(server)

    encText = urllib.parse.quote(InputLabel.get())

    if num==11:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=2010&yearto=2018&&query=" + encText, None,
                    {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num==12:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=2000&yearto=2009&&query=" + encText, None,
                    {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num == 13:
        conn.request("GET",
                     "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1990&yearto=1999&&query=" + encText, None,
                     {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num == 14:
        conn.request("GET",
                     "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1980&yearto=1989&&query=" + encText, None,
                     {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num == 15:
        conn.request("GET",
                     "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1970&yearto=1979&&query=" + encText, None,
                     {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num==16:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1960&yearto=1969&&query=" + encText, None,
                    {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num==17:
        conn.request("GET", "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1950&yearto=1959&&query=" + encText, None,
                    {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num == 18:
        conn.request("GET",
                     "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1940&yearto=1949&&query=" + encText, None,
                     {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num == 19:
        conn.request("GET",
                     "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1930&yearto=1939&&query=" + encText, None,
                     {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret})
    elif num == 20:
        conn.request("GET",
                     "/v1/search/movie.xml?movie&display=100&start=1&yearfrom=1920&yearto=1929&&query=" + encText, None,
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

    RenderText.insert(INSERT, "< 전체 >")
    if num==11:
        RenderText.insert(INSERT, "< 2010 ~ 2018 > ");
    if num==12:
        RenderText.insert(INSERT, "< 2000 ~ 2009 > ");
    if num==13:
        RenderText.insert(INSERT, "< 1990 ~ 1999 > ");
    if num==14:
        RenderText.insert(INSERT, "< 1980 ~ 1989 > ");
    if num==15:
        RenderText.insert(INSERT, "< 1970 ~ 1979 > ");
    if num==16:
        RenderText.insert(INSERT, "< 1960 ~ 1969 > ");
    if num==17:
        RenderText.insert(INSERT, "< 1950 ~ 1959 > ");
    if num==18:
        RenderText.insert(INSERT, "< 1940 ~ 1949 > ");
    if num==19:
        RenderText.insert(INSERT, "< 1930 ~ 1939 > ");
    if num==20:
        RenderText.insert(INSERT, "< 1920 ~ 1929 > ");

    for i in range(len(DataList)):
        if DataList != []:
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")
                # for j in range(0, 7):
            RenderText.insert(INSERT, "[")
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


def Rating6():
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
            DataList.append(a.findtext('title'))
            #DataList.append(a.findtext('pubDate'))
            #DataList.append(a.findtext('director'))
            #DataList.append(a.findtext('actor'))
            DataList.append(a.findtext('userRating'))

    for i in range(len(DataList)):
        if DataList[i]=='6.00':
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "]")
            RenderText.insert(INSERT, "제목 : ")
            RenderText.insert(INSERT, DataList[i-1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n")







##########################################################################################################################################

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="[영화 검색 App]")
    MainText.place(x=200,y=20)


def image():
    photo = PhotoImage(file="picture.gif")  # 디폴트 이미지 파일
    imageLabel = Label(window, image=photo)
    imageLabel.configure(image=photo)
    imageLabel.image = photo
    imageLabel.place(x=130,y=530)


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
