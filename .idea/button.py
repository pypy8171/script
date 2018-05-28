from tkinter import*
import Movie

window = Tk()
def process():
    movie = (e1.get())
    e2.insert(0,movie)

def reset():
    empty = (e3.get())
    e2.insert(0,empty)



l1 = Label(window, text="영화 장르 입력 : ", font = 'helvetica 12 italic')
l2 = Label(window, text="결과", font = 'helvetica 12 italic')
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)


b1 = Button(window, text="검색",command=process)
b1.grid(row=0,column=3); b1["bg"]="yellow"

b2 = Button(window, text="초기화",command=reset)
b2.grid(row=1,column=3); b2["bg"]="yellow"
window.mainloop()