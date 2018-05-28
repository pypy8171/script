from tkinter import*
from tkinter import font
import tkinter.messagebox
import Movie

window = Tk()
window.geometry("400x600+750+200")
DataList = []

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family = 'Consolas')
    MainText = Label(window, font = TempFont, text="[영화 검색 App]")
    MainText.place(x=80,y=20)

def process():
    movie = (e1.get())
    #e2.insert(0,movie)
    e2.search(0,movie)

def reset():
    e2.delete(0,100)
    e1.delete(0,100)



l1 = Label(window, text="영화 장르 입력 : ", font = 'helvetica 12 italic')
l2 = Label(window, text="결과", font = 'helvetica 12 italic')
l1.place(x=0,y=100)
l2.place(x=40,y=150)

e1 = Entry(window)
e2 = Entry(window)
e1.place(x=130,y=100)
e2.place(x=130,y=150)

b1 = Button(window, text="검색",command=process)
b1.grid(row=0,column=3); b1["bg"]="yellow"
b1.place(x=300,y=100)

b2 = Button(window, text="초기화",command=reset)
b2.grid(row=1,column=3); b2["bg"]="yellow"
b2.place(x=300,y=150)


InitTopText()
window.mainloop()
