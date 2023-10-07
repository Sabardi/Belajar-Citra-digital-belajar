import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
#membuat fungsi untuk dialog pemilihan gambar
def Open_image():
    file_path = filedialog.askopenfilename(filetypes=[("image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)

        #menampilkan gambar pada jendela GUI
        label.config(image=photo)
        label.image = photo

#membuat jendela Tkinter
root = tk.Tk()
root.title("pemilihan dan tampilan gambar")

#tombol untuk membuka gambar
open_button = tk.Button(root, text="Buka gambar", command=Open_image)
open_button.pack(pady=10)

# label untuk menampilkan gambar
label = tk.Label(root)
label.pack()

#menjalankan Gui
root.mainloop()


