# Import module
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import threading
from play_videos import MainWindow
from  train_and_test  import VideoCaptioning
import cv2


class lord:
    def __init__(self, root):
        self.root = root

        self.root.geometry('1200x800+350+150')
        self.root.title(" VIDEO DESCRIPTION ")
        self.canvas = Canvas(root)

        self.image = PhotoImage(file=r"C:\Users\ali12\Desktop\lord.png")

        self.canvas.create_image(0, 0, image=self.image, anchor=NW)
        self.canvas.pack(side=TOP, fill=BOTH,pady=5, expand=1)
        self.button = Button(self.canvas, text=" Exit Program ", width=110, height=2, bg="lavender", command=root.destroy,
                             relief=RAISED, bd=7, font=('Arial', 15))
        self.button.pack(side=BOTTOM,fill=X)

        self.frame=Frame(self.canvas,bg="lavender",bd=5)
        self.frame.pack(fill=X)
        self.button1 = Button(self.frame,command=lambda : self.newthread(self.top_level(),None), text=" play video ", bd=7, height=2, width=27, bg="lavender", font=('Arial', 15))
        self.button1.pack(side=LEFT,anchor="n",pady=5,fill=X,expand=1)
        self.button2 = Button(self.frame,command=lambda : self.newthread(self.get_file_path_for_npy(),None), text=" Generate Caption ", width=30, height=2, bd=7, bg="lavender", font=('Arial', 15))
        self.button2.pack(side=LEFT,anchor="n",pady=5,fill=X,expand=1)
        self.label = Label(self.canvas, width=100, height=2, bd=7, bg="lavender", font=('Arial', 15))

        self.video=None
        self.button.bind("<Motion>", lambda x: self.press(self.button))
        self.button.bind("<Leave>", lambda x: self.unpress(self.button))
        self.button1.bind("<Motion>", lambda x: self.press(self.button1))
        self.button1.bind("<Leave>", lambda x: self.unpress(self.button1))
        self.button2.bind("<Motion>", lambda x: self.press(self.button2))
        self.button2.bind("<Leave>", lambda x: self.unpress(self.button2))


    def top_level(self):
        file_path = filedialog.askopenfilename()
        self.top=Toplevel(self.root)
        if file_path:
            MainWindow(self.top, cv2.VideoCapture(file_path))
            self.top.mainloop()


    def on_click(self,x):
        x.destroy()
    def get_file_path_for_npy(self):

        file_path= filedialog.askopenfilename()
        if file_path :
           v=VideoCaptioning(mode="test")
           ll=[]
           ll.append(file_path)
           caption=v.inference(ll)
           self.label.config(text=caption)
           self.label.pack(side=BOTTOM, pady=100)
           self.button2.bind("<Button-1>", lambda x: self.on_click(self.label))






    def newthread(self,func,arg):
        self.thread = threading.Thread(target=func,args=arg)
        self.thread.daemon = 1
        self.thread.start()

    def press(self, x):
        x.config(relief=GROOVE)
        x.config(bg="steelblue", fg="lightcyan")

    def unpress(self, x):
        x.config(relief=RAISED)
        x.config(bg="lavender", fg="black")


root = Tk()
lordy = lord(root)
root.mainloop()

