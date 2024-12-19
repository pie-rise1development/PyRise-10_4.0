import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageFilter, ImageTk

class PhotoEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Pie-Rise // PhotoEditor 1")

        self.image_label = tk.Label(master, text="Найдите изображение, с чем хотите провести редакцию!")
        self.image_label.pack()

        self.canvas = tk.Canvas(master, width=400, height=300)
        self.canvas.pack()

        self.load_button = tk.Button(master, text="Выберите нужное изображение...", command=self.load_image)
        self.load_button.pack()

        self.blur_button = tk.Button(master, text="Применить эффект размытия", command=self.blur_image)
        self.blur_button.pack()

        self.sharpen_button = tk.Button(master, text="Добавить резкость", command=self.sharpen_image )
        self.sharpen_button.pack()

        self.save_button = tk.Button(master, text="Сохранить как готовое изображение.", command=self.save_image)
        self.save_button.pack()

        self.image = None
        self.file_path = None

    def load_image(self):
        self.file_path = filedialog.askopenfilename(title="Пожалуйста выберите изображение, ведь без этого никак!", filetypes=[("Image files", "*,jpg;*.jpeg;*.png")])
        if self.file_path:
            self.image = Image.open(self.file_path)
            self.display_image(self.image)

    def display_image(self, img):
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def blur_image(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)
            self.display_image(self.image)
        else:
            messagebox.showwarning("Ошибочка!", "Вам нужно загрузить изображение, которые вы хотите начать редактировать.")

    def sharpen_image(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.SHARPEN)
            self.display_image(self.image)
        else:
            messagebox.showwarning("Ошибочка!", "Вам нужно загрузить изображение, которые вы хотите начать редактировать.")

    def save_image(self):
        if self.image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
            if save_path:
                self.image.save(save_path)
                messagebox.showinfo("Внимание!", "Изображение, что вы редактировали было успешно сохранено.")
        else:
            messagebox.showwarning("Ошибочка!", "Вам нужно загрузить изображение, которые вы хотите начать редактировать.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = PhotoEditor(root)
    root.mainloop()
