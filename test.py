
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("runs/detect/train10/weights/best.pt")
    metrics = model.val()
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps  # a list contains map50-95 of each category
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import ttk
# from PIL import Image, ImageTk
# from ultralytics import YOLO
# import matplotlib.pyplot as plt
# import cv2
# import torch
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow.keras.models import load_model
# import customtkinter as ctk
#
# def load_and_process_image(image_path, model):
#     img = image.load_img(image_path, target_size=(2432, 2432))
#     img = image.img_to_array(img)
#     img = img.astype('float32')  # Явное преобразование к типу float32
#     img = img / 255.0  # Нормализация
#     img = np.expand_dims(img, axis=0)  # Добавление размерности пакета
#     reconstructed_img = model.predict(img)  # Восстановление изображения с помощью модели
#     return img[0], reconstructed_img[0]
#
#
# # Функция для выявления аномалий на изображении
# def detect_anomalies(original, reconstructed, threshold):
#     difference = np.abs(original - reconstructed)
#     anomaly_mask = difference > threshold
#     return anomaly_mask
#
#
# def load_image1():
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         image = Image.open(file_path)
#         image = image.resize((350, 300))
#         photo = ImageTk.PhotoImage(image)
#         label_image1.configure(image=photo)
#         label_image1.image = photo
#         label_text1.configure(text="загруженное Изображение")
#         selected_item = combo_box.get()
#         if selected_item == 'YOLO':
#             # img = cv2.imread("C:/Users/kimsl/VKR/PCB_DATASET/images/Missing_hole/04_missing_hole_01.jpg")
#             img = cv2.imread(file_path)
#             model = YOLO("runs/detect/train10/weights/best.pt")
#             results = model(img, imgsz=1080, iou=0.4, conf=0.55, verbose=True)
#             annotated_frame = results[0].plot()
#             image_cv2 = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
#             image_pil = Image.fromarray(image_cv2)
#             image_pil = image_pil.resize((350, 300))
#             photo = ImageTk.PhotoImage(image_pil)
#             label_image2.configure(image=photo)
#             label_image2.image = photo
#             label_text2.configure(text="YOLO")
#
#         if selected_item == 'Автоэнкодер':
#             # Путь к изображению
#             image_path = file_path
#
#             # Загрузка модели автоэнкодера
#             autoencoder = load_model("autoencoder_model.h5")
#             # Загрузка и обработка изображения
#             original_image, reconstructed_image = load_and_process_image(image_path, autoencoder)
#
#             # Задание порога для определения аномалий
#             threshold = 0.15  # Пример значения порога, может потребоваться настройка в зависимости от данных
#
#             # Конвертируем массив в изображение PIL
#             neural_net_image = (reconstructed_image * 255).astype(np.uint8)
#             image_pil = Image.fromarray(neural_net_image)
#             image_pil = image_pil.resize((350, 300))
#             photo = ImageTk.PhotoImage(image_pil)
#             label_image3.configure(image=photo)
#             label_image3.image = photo
#             label_text3.configure(text="сгенерированное изображение")
#
#             # Выявление аномалий на изображении
#             anomaly_mask = detect_anomalies(original_image, reconstructed_image, threshold)
#             anomaly_mask = (anomaly_mask * 255).astype(np.uint8)
#             image_pil = Image.fromarray(anomaly_mask)
#             image_pil = image_pil.resize((350, 300))
#             photo = ImageTk.PhotoImage(image_pil)
#             label_image4.configure(image=photo)
#             label_image4.image = photo
#             label_text4.configure(text="маска")
#
#
# def on_combobox_select(event):
#     selected_item = combo_box.get()
#     print(f"Selected: {selected_item}")
#     return selected_item
#
# # Создаем главное окно
# root = ctk.CTk()
# root.title(" UI ")
#
# # Создаем кнопки
# button1 = ctk.CTkButton(root, text="Загрузить изображение", command=load_image1)
# button1.grid(row=0, column=0, padx=10, pady=10)
#
# # Создаем выпадающий список (ComboBox)
# combo_box = ctk.CTkComboBox(root, values=["YOLO", "Автоэнкодер"])
# combo_box.set("YOLO")  # Устанавливаем значение по умолчанию
# combo_box.grid(row=0, column=1, padx=10, pady=10)
# combo_box.bind("<<ComboboxSelected>>", on_combobox_select)
#
#
# # Место для изображений и текста
# label_image1 = ctk.CTkLabel(root, text="")
# label_image1.grid(row=1, column=0, padx=10, pady=10)
# label_text1 = ctk.CTkLabel(root, text="")
# label_text1.grid(row=2, column=0, padx=10, pady=5)
#
# label_image2 = ctk.CTkLabel(root, text="")
# label_image2.grid(row=1, column=1, padx=10, pady=10)
# label_text2 = ctk.CTkLabel(root, text="")
# label_text2.grid(row=2, column=1, padx=10, pady=5)
#
# label_image3 = ctk.CTkLabel(root, text="")
# label_image3.grid(row=3, column=0, padx=10, pady=10)
# label_text3 = ctk.CTkLabel(root, text="")
# label_text3.grid(row=4, column=0, padx=10, pady=5)
#
# label_image4 = ctk.CTkLabel(root, text="")
# label_image4.grid(row=3, column=1, padx=10, pady=10)
# label_text4 = ctk.CTkLabel(root, text="")
# label_text4.grid(row=4, column=1, padx=10, pady=5)
# # Запуск основного цикла приложения
# root.mainloop()