import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class CameraApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplikasi Kamera")
        
        self.camera = cv2.VideoCapture(0)
        
        self.image_label = tk.Label(self.root)
        self.image_label.pack()
        
        self.capture_button = tk.Button(self.root, text="Ambil Gambar", command=self.capture_image)
        self.capture_button.pack(pady=10)
        
        self.open_button = tk.Button(self.root, text="Pilih Gambar", command=self.open_file_dialog)
        self.open_button.pack(pady=10)
        
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18))
        self.result_label.pack()
        
        self.show_camera()
        
        self.root.mainloop()
        
    def show_camera(self):
        ret, frame = self.camera.read()
        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            self.display_image(image)
            self.root.after(10, self.show_camera)
        else:
            self.result_label.config(text="Gagal membaca frame")
        
    def capture_image(self):
        ret, frame = self.camera.read()
        if ret:
            cv2.imwrite("captured_image.jpg", frame)
            self.result_label.config(text="Gambar berhasil diambil")
        else:
            self.result_label.config(text="Gagal mengambil gambar")
            
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            self.display_image(image)
            self.result_label.config(text="")
            
    def display_image(self, image):
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.photo = photo

# Membuat objek aplikasi kamera
app = CameraApp()