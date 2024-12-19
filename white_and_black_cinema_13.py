from tkinter import *
import PIL
from PIL import Image, ImageDraw
from tkinter import messagebox
from random import *


def save():
    filename = f"image_{randint(0, 10000)}.png"
    image1.save(filename)
    messagebox.showinfo("Подготовка!", "Файл сохранён, его название: %s" % filename)


def activate_paint(event):
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    cv.create_line(x1, y1, x2, y2, fill = 'white', width=5)
    draw.line((x1, y1, x2, y2), fill = 'white', width = 5)


root = Tk()
root.title("Pie-Rise Depicture-1")
root.resizable(width=False, height=False)
root.iconbitmap("Sound's/paint.ico")


cv = Canvas(root, width=1280, height=720, bg='black')

image1 = PIL.Image.new('RGB', (1280, 720), 'black')
draw = ImageDraw.Draw(image1)

cv.bind('<B1-Motion>', activate_paint)
cv.pack(expand=1, fill=BOTH)

btn_save = Button(text="save", command=save, bg='white', fg='black', font=('Comic Sans MS', 30))
btn_save.pack()

root.mainloop()