import tkinter as tk
from PIL import Image, ImageTk
import cv2
class MainWindow():
    def __init__(self, window, cap):
        self.window = window
        self.window.title("play videos ")
        self.window.geometry('1200x800+350+150')
        self.cap = cap

        self.width = 1200
        self.height = 800
        print(self.width)
        print(self.height)
        self.interval = 20 # Interval in ms to get the latest frame
        # Create canvas for image
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        self.canvas.grid(row=0, column=0)
        # Update image on canvas
        self.update_image()
    def update_image(self):
        # Get the latest frame and convert image format
        self.image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB) # to RGB
        self.image = cv2.resize(self.image,(1200,800))
        self.image = Image.fromarray(self.image) # to PIL format
        self.image = ImageTk.PhotoImage(self.image) # to ImageTk format
        # Update image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        # Repeat every 'interval' ms
        self.window.after(self.interval, self.update_image)
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root, cv2.VideoCapture(r"D:\zip_files\TestVideo\video7011.mp4"))
    root.mainloop()