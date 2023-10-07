import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk


class BukaGambar:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing")

        # Tombol untuk memilih gambar
        self.select_button = ttk.Button(root, text="Pilih Gambar", command=self.select_image)
        self.select_button.pack(pady=10)

        # Label untuk menampilkan gambar
        self.label = ttk.Label(root)
        self.label.pack(padx=10, pady=10)

        # Variabel untuk menyimpan path gambar yang dipilih
        self.image_path = ""

        # Menu dropdown untuk transformasi gambar
        self.transform_menu = ttk.Combobox(root, values=["Grayscale", "Blur", "Rotate"])
        self.transform_menu.pack()

        # Tombol untuk menerapkan transformasi
        self.transform_button = ttk.Button(root, text="Terapkan Transformasi", command=self.apply_transform)
        self.transform_button.pack(pady=10)

    def select_image(self):
        # Membuka dialog pemilihan gambar dan mendapatkan path gambar
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
        # Memeriksa apakah path gambar valid
        if self.image_path:
            self.display_image()

    def display_image(self):
        # Membaca gambar dari path dan menampilkannya di label
        image = Image.open(self.image_path)
        photo = ImageTk.PhotoImage(image=image)
        self.label.config(image=photo)
        self.label.image = photo  # Menyimpan referensi agar gambar tetap ditampilkan

    def apply_transform(self):
        # Mengambil nilai transformasi yang dipilih
        selected_transform = self.transform_menu.get()
        # Memeriksa apakah gambar telah dipilih
        if not self.image_path:
            return
        # Membaca gambar dari path
        image = cv2.imread(self.image_path)
        # Melakukan transformasi sesuai dengan pilihan
        if selected_transform == "Grayscale":
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif selected_transform == "Blur":
            image = cv2.GaussianBlur(image, (15, 15), 0)
        elif selected_transform == "Rotate":
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        # Menampilkan gambar yang telah ditransformasi
        cv2.imshow("Gambar yang Ditransformasi", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = BukaGambar(root)
    app.run()