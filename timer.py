#!/usr/bin/env python

from tkinter import *
import time

root = Tk()
root.title("5-Flag Chess Clock")

mainBackground = "light blue"

root.geometry("950x360+0+0")
root.configure(background=mainBackground)

Display1 = Label(root, font=("Typewriter", 60), bg="light yellow")
Display1.place(x=50, y=50, width=200, height=150)

Display2 = Label(root, font=("Typewriter", 60), bg="light yellow")
Display2.place(x=300, y=50, width=200, height=150)

Display3 = Label(root, font=("Typewriter", 60), bg="light yellow")
Display3.place(x=550, y=50, width=200, height=150)

Display4 = Label(root, font=("Typewriter", 60), bg="light yellow")
Display4.place(x=800, y=50, width=200, height=150)

Display5 = Label(root, font=("Typewriter", 60), bg="light yellow")
Display5.place(x=1050, y=50, width=200, height=150)

Label1 = Label(root, font=("System", 18), anchor=W, bg=mainBackground)
Label1.place(x=50, y=20, width=200)
Label1.config(text='1 to press clock')

Label2 = Label(root, font=("System", 18), anchor=E, bg=mainBackground)
Label2.place(x=300, y=20, width=200)
Label2.config(text='2 to press clock')

Label3 = Label(root, font=("System", 18), anchor=E, bg=mainBackground)
Label3.place(x=550, y=20, width=200)
Label3.config(text='3 to press clock')

Label4 = Label(root, font=("System", 18), anchor=E, bg=mainBackground)
Label4.place(x=800, y=20, width=200)
Label4.config(text='4 to press clock')

Label5 = Label(root, font=("System", 18), anchor=E, bg=mainBackground)
Label5.place(x=1050, y=20, width=200)
Label5.config(text='5 to press clock')

modeLabel = Label(root, font=("System", 18), anchor=W, bg=mainBackground)
modeLabel.place(x=50, y=200, width=200)
modeLabel.config(text="Mode: Athish")


def reset_display():
    Display1.config(fg="black")
    Display2.config(fg="black")
    Display3.config(fg="black")
    Display4.config(fg="black")
    Display5.config(fg="black")
    Label1.config(text="1 to press clock")
    Label2.config(text="2 to press clock")
    Label3.config(text="3 to press clock")
    Label4.config(text="4 to press clock")
    Label5.config(text="5 to press clock")


classicalString = "Classical: 9 min"

def classical_callback():
    if g.paused or g.gameOver or (not g.Running1 and not g.Running2 and not g.Running3 and not g.Running4 and not g.Running5):
        g.new_classical()
        reset_display()
        modeLabel.config(text="Mode: Classical")
        Display1.config(fg="dark green")
        Display2.config(fg="dark green")
        Display3.config(fg="dark green")
        Display4.config(fg="dark green")
        Display5.config(fg="dark green")



classicalButton = Button(root, text=classicalString,
                         highlightbackground=mainBackground,
                         command=classical_callback)
classicalButton.place(x=50, y=240, width=400)
classicalButton.config(bg="green")




#def revert_callback():

def enable_modes():
    classicalButton.config(state=NORMAL)


def disable_modes():
    classicalButton.config(state=DISABLED)


class Game:
    def __init__(self):
        self.Time1, self.Time2 ,self.Time3, self.Time4,self.Time5 = 540, 540, 540,540,540
        self.reference = 0
        self.Running1, self.Running2, self.Running3,self.Running4,self.Running5, self.paused = TRUE, FALSE, FALSE , FALSE ,FALSE,TRUE
        self.start=FALSE


    def new_classical(self):
        self.Time1, self.Time2 ,self.Time3, self.Time4,self.Time5 = 540, 540, 540,540,540
        self.reference = 0
        self.Running1, self.Running2, self.Running3,self.Running4,self.Running5, self.paused = TRUE, FALSE, FALSE , FALSE ,FALSE,TRUE
        self.start=FALSE


g = Game()


def key_pressed(event):

    if event.char == '1' and not g.paused and g.Running5:
        disable_modes()
        g.Running5 = FALSE
        Label1.configure(text="")       
        g.reference = g.Time1 + time.time()
        g.Running1 = TRUE
        Label2.configure(text="2 to press clock")

    if event.char == '2' and not g.paused and g.Running1 :
        disable_modes()
        g.Running1 = FALSE
        Label2.configure(text="")
        g.reference = g.Time2 + time.time()
        g.Running2 = TRUE
        Label3.configure(text="3 to press clock")
    if event.char == '3' and not g.paused and g.Running2 :
        disable_modes()
        g.Running2 = FALSE
        Label3.configure(text="")
        g.reference = g.Time3 + time.time()
        g.Running3 = TRUE
        Label4.configure(text="4 to press clock")
    if event.char == '4' and not g.paused and g.Running3:
        disable_modes()
        g.Running3 = FALSE
        Label4.configure(text="")
        g.reference = g.Time4 + time.time()
        g.Running4 = TRUE
        Label5.configure(text="5 to press clock")
    if event.char == '5' and not g.paused and g.Running4 :
        disable_modes()
        g.Running4 = FALSE
        Label5.configure(text="")
        g.reference = g.Time5 + time.time()
        g.Running5 = TRUE
        Label1.configure(text="1 to press clock")
    


    if event.char == ' ' and (g.Running1 or g.Running2 or g.Running3 or g.Running4 or g.Running5):
        g.paused = not g.paused
        if g.paused:
            enable_modes()
        else:
            disable_modes()
        if not g.paused and g.Running1:
            Label2.configure(text="2 to press clock")
            g.reference = g.Time1 + time.time()
        if not g.paused and g.Running2:
            Label3.configure(text="3 to press clock")
            g.reference = g.Time2 + time.time()
        if not g.paused and g.Running3:
            Label4.configure(text="4 to press clock")
            g.reference = g.Time3 + time.time()
        if not g.paused and g.Running4:
            Label5.configure(text="5 to press clock")
            g.reference = g.Time4 + time.time()   
        if not g.paused and g.Running5:
            Label1.configure(text="1 to press clock")
            g.reference = g.Time5 + time.time()   
            
                
        if g.paused and g.Running1:
            Label1.configure(text="Paused")
        if g.paused and g.Running2:
            Label2.configure(text="Paused")
                
        if g.paused and g.Running3:
            Label3.configure(text="Paused")
        if g.paused and g.Running4:
            Label4.configure(text="Paused")
                
        if g.paused and g.Running5:
            Label5.configure(text="Paused")


root.bind("<Key>", key_pressed)


def update_clock():
    if (g.Running1 and not g.paused ) :
        g.Time1 = g.reference - time.time()


    if (g.Running2 and not g.paused ) :
        g.Time2 = g.reference - time.time()

    if (g.Running3 and not g.paused) :
        g.Time3 = g.reference - time.time()
    if (g.Running4 and not g.paused ):
        g.Time4 = g.reference - time.time()
    if ( g.Running5 and not g.paused ) :
        g.Time5 = g.reference - time.time()
        
    m1 = int(g.Time1 / 60) % 60
    s1 = int(g.Time1) % 60
    t1 = int(g.Time1 * 10) % 10
    m2 = int(g.Time2 / 60) % 60
    s2 = int(g.Time2) % 60
    t2 = int(g.Time2 * 10) % 10
    m3 = int(g.Time3 / 60) % 60
    s3 = int(g.Time3) % 60
    t3 = int(g.Time3 * 10) % 10
    m4 = int(g.Time4 / 60) % 60
    s4 = int(g.Time4) % 60
    t4 = int(g.Time4 * 10) % 10
    m5 = int(g.Time5 / 60) % 60
    s5 = int(g.Time5) % 60
    t5 = int(g.Time5 * 10) % 10

    Display1.config(text=f'{m1:01}' + '.' + f'{s1:02}')


    Display2.config(text=f'{m2:01}' + '.' + f'{s2:02}')



    Display3.config(text=f'{m3:01}' + '.' + f'{s3:02}')


    Display4.config(text=f'{m4:01}' + '.' + f'{s4:02}')



    Display5.config(text=f'{m5:01}' + '.' + f'{s5:02}')


    
    root.after(20, update_clock)  # run itself after given number of milliseconds


# run first time
update_clock()

root.mainloop()



