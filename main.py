from tkinter import *
import random
def draw_set(the_canvas):
    the_canvas.delete("all")
    the_canvas.create_line(0,150, 150, 150, fill="black")
    the_canvas.create_line(150,150, 150, 350, fill="black")
    the_canvas.create_line(40,150, 40, 20, fill="black")
    the_canvas.create_line(40,20, 60, 10, fill="black")
    the_canvas.create_line(60,10, 120, 10, fill="black")
    the_canvas.create_line(120,10, 130, 15, fill="black")
    the_canvas.create_line(130,15, 130, 25, fill="black")
    the_canvas.create_line(130,25,120, 30, fill="black")
    the_canvas.create_line(115,30, 115, 50, fill="black")
    the_canvas.create_line(120,30, 60, 30, fill="black")
    the_canvas.create_line(70,30, 60, 40, fill="black")
    the_canvas.create_line(80,30, 60, 50, fill="black")
    the_canvas.create_line(60,30, 60, 150, fill="black")
    the_canvas.create_line(60,130, 80,150, fill="black")
    the_canvas.create_line(40,130, 20,150, fill="black")
def start_game(the_canvas):
    if(list_of_letters!=[]):
        for i in list_of_letters:
            i.destroy()
    draw_set(the_canvas)
    create_alphabet()
    victory.configure(text="")
    hiddenword,blanks=create_hidden_word()
    newblanks_label.configure(text="",font=("fixedsys",30),bg="#eefd98")
    blanks_label.configure(text=blanks,font=("fixedsys",30),bg="#eefd98")
def letter_input(letter,oldblanks,hiddenword,incorrect,the_canvas,button_pressed):
    if(letter in hiddenword):
        for i in range(len(hiddenword,)):
            if(hiddenword[i]==letter):
                oldblanks=oldblanks[:i]+letter+oldblanks[i+1:]
        newblanks_label.configure(text=oldblanks,font=("fixedsys",30),bg="#eefd98")
        if(oldblanks==hiddenword):
            victory.configure(text="YOU WIN!",font=("fixedsys",20))
            victory.place(x=290,y=70)
            for i in list_of_letters:
                i.destroy()
    else:
        wrong_guess(incorrect,the_canvas)
    global blanks
    blanks=oldblanks
    button_pressed.destroy()
def wrong_guess(wrong,the_canvas):
    if(wrong==0):
        the_canvas.create_oval(100,50, 130, 70, fill="black")
    if(wrong==1):
        the_canvas.create_line(115,50, 115, 120, fill="black")
    if(wrong==2):
        the_canvas.create_line(115,90,130,100)
    if(wrong==3):
        the_canvas.create_line(115,90,100,100)
    if(wrong==4):
        the_canvas.create_line(115,120,130,140)
    if(wrong==5):
        the_canvas.create_line(115,120,100,140)
        victory.configure(text="YOU LOSE!",font=("fixedsys",20))
        victory.place(x=290,y=70)
        for i in list_of_letters:
                i.destroy()
        newblanks_label.configure(text=hiddenword)
    global incorrect
    incorrect=wrong+1
def create_hidden_word():
    global hiddenword
    global blanks
    global incorrect
    incorrect=0
    words=["CLOUD","TODAY","TOMORROW","RANDOM","DEVELOPER","WHENEVER","YES",
           "BREAKFAST","MATH","SCIENCE","COOKING","FUNNY","YES","KEYBOARD",
           "FORWARD","BACKWARDS","CONSOLE","GAME","PYTHON","GLASSES",
           "TOMATOE","KITCHEN","WORDS","GARBAGE","GLASS","CRINGE","CHIPS","CASINO",
           "TABLE","MEATLOAF","PASTA","APPLICATION","EQUAL","DOWNLOAD"]
    randnum=random.randint(0,len(words)-1)
    hiddenword=words[randnum]
    blanks="_"*len(hiddenword)
    return hiddenword,blanks
def startscreen(the_canvas):
    Start=Button(window,text="PLAY",padx=54,pady=30,bg="#b3ffb5",font=("fixedsys",10),command=lambda: start_game(the_canvas))
    global list_of_letters
    list_of_letters=[]
    Start.place(x=0,y=233)
    draw_set(the_canvas)
def create_alphabet():
    A=Button(window,text="A",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("A",blanks,hiddenword,incorrect,the_canvas,A))
    A.place(x=160,y=200)
    B=Button(window,text="B",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("B",blanks,hiddenword,incorrect,the_canvas,B))
    B.place(x=200,y=200)
    C=Button(window,text="C",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("C",blanks,hiddenword,incorrect,the_canvas,C))
    C.place(x=240,y=200)
    D=Button(window,text="D",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("D",blanks,hiddenword,incorrect,the_canvas,D))
    D.place(x=280,y=200)
    E=Button(window,text="E",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("E",blanks,hiddenword,incorrect,the_canvas,E))
    E.place(x=320,y=200)
    F=Button(window,text="F",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("F",blanks,hiddenword,incorrect,the_canvas,F))
    F.place(x=360,y=200)
    G=Button(window,text="G",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("G",blanks,hiddenword,incorrect,the_canvas,G))
    G.place(x=400,y=200)
    H=Button(window,text="H",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("H",blanks,hiddenword,incorrect,the_canvas,H))
    H.place(x=440,y=200)
    I=Button(window,text="I",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("I",blanks,hiddenword,incorrect,the_canvas,I))
    I.place(x=480,y=200)
    J=Button(window,text="J",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("J",blanks,hiddenword,incorrect,the_canvas,J))
    J.place(x=520,y=200)
    K=Button(window,text="K",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("K",blanks,hiddenword,incorrect,the_canvas,K))
    K.place(x=560,y=200)
    L=Button(window,text="L",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("L",blanks,hiddenword,incorrect,the_canvas,L))
    L.place(x=600,y=200)
    M=Button(window,text="M",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("M",blanks,hiddenword,incorrect,the_canvas,M))
    M.place(x=640,y=200)
    N=Button(window,text="N",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("N",blanks,hiddenword,incorrect,the_canvas,N))
    N.place(x=160,y=250)
    O=Button(window,text="O",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("O",blanks,hiddenword,incorrect,the_canvas,O))
    O.place(x=200,y=250)
    P=Button(window,text="P",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("P",blanks,hiddenword,incorrect,the_canvas,P))
    P.place(x=240,y=250)
    Q=Button(window,text="Q",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("Q",blanks,hiddenword,incorrect,the_canvas,Q))
    Q.place(x=280,y=250)
    R=Button(window,text="R",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("R",blanks,hiddenword,incorrect,the_canvas,R))
    R.place(x=320,y=250)
    S=Button(window,text="S",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("S",blanks,hiddenword,incorrect,the_canvas,S))
    S.place(x=360,y=250)
    T=Button(window,text="T",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("T",blanks,hiddenword,incorrect,the_canvas,T))
    T.place(x=400,y=250)
    U=Button(window,text="U",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("U",blanks,hiddenword,incorrect,the_canvas,U))
    U.place(x=440,y=250)
    V=Button(window,text="V",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("V",blanks,hiddenword,incorrect,the_canvas,V))
    V.place(x=480,y=250)
    W=Button(window,text="W",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("W",blanks,hiddenword,incorrect,the_canvas,W))
    W.place(x=520,y=250)
    X=Button(window,text="X",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("X",blanks,hiddenword,incorrect,the_canvas,X))
    X.place(x=560,y=250)
    Y=Button(window,text="Y",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("Y",blanks,hiddenword,incorrect,the_canvas,Y))
    Y.place(x=600,y=250)
    Z=Button(window,text="Z",padx=10,pady=10,bg="#b3ffb5",font=("fixedsys",10),command=lambda:letter_input("Z",blanks,hiddenword,incorrect,the_canvas,Z))
    Z.place(x=640,y=250)
    global list_of_letters
    list_of_letters=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
window=Tk()
window.title("Hangman")
window.geometry("700x300")
window.configure(bg="#eefd98")
title=Label(text="HANGMAN",font=("fixedsys",50),bg="#eefd98")
title.pack(side=TOP)
victory=Label(text="",bg="#eefd98")
victory.place(x=290,y=70)
canvas_width = 200
canvas_height = 275
the_canvas = Canvas(window,width=canvas_width,height=canvas_height, highlightthickness=0)
the_canvas.configure(bg="#eefd98")
the_canvas.pack(side=LEFT)
blanks_label=Label(text="",font=("fixedsys",30),bg="#eefd98")
blanks_label.place(x=160,y=130)
newblanks_label=Label(text="",font=("fixedsys",30),bg="#eefd98")
newblanks_label.place(x=160,y=130)
startscreen(the_canvas)
window.mainloop()
