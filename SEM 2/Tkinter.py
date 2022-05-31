from tkinter import *

class Start:
    def __init__(self, Frame):
        self.SubFrame1 = Frame
        self.SubFrame1.title('Started')
    
    def tampilan(self):
        canvas1 = Canvas(self.SubFrame1, width=400, height=500, relief=RAISED, bg='black')
        canvas1.grid()

        self.fotoBG = PhotoImage(file='BG.png')
        display1 = Label(self.SubFrame1, image=self.fotoBG, bg='black')
        canvas1.create_window(200, 180, window=display1)

        Bt1 = Button(self.SubFrame1, text="Get Started", command=self.lanjut, width=30, relief=RIDGE, font='SedanSC 11 normal', bg='white', borderwidth=0, height=2)
        canvas1.create_window(200, 400, window=Bt1)

    def lanjut(self):
        pass    
def main_program():
    main = Tk()
    main_login = Start(main)
    main_login.tampilan()
    main.mainloop()


main_program()

# from tkinter import *
# window= Tk()
# def button1clicked():
#     print("button1 cliced")
# def invokebutton1():
#     button1.invoke()
# button1=Button(window,text="button1", command=button1clicked)
# button1.pack()
 
# button2=Button(window,text="button2", command=invokebutton1)
# button2.pack()
 
 
# window.mainloop()