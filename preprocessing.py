
import cv2
import os

#  путь к папке с изображениями
path_data_in = 'C:/Users/kimsl/VKR/PCB_DATASET/PCB_USED'
path_data_out = 'C:/Users/kimsl/VKR/2'


"""Нарезка изображений"""
#  размер сетки
grid = (4, 4)
num_img = 1

# Пройтись по всем изображениям в папке
for img_name in os.listdir(path_data_in):
    # Пропустить, если это не изображение
    # if not img_name.endswith(".jpg") and not img_name.endswith(".png"):
    #     print(1)
    #     continue

    # Загрузить изображение
    img = cv2.imread(os.path.join(path_data_in, img_name))

    # Высота и ширина изображения
    height, width, _ = img.shape

    # Разделить изображение на сетку
    width_new = width // grid[0]
    height_new = height // grid[1]

    # Пройтись по ячейкам сетки
    for y in range(grid[1]):
        for x in range(grid[0]):
            # Вырезать часть изображения
            new_img = img[y * height_new:(y + 1) * height_new, x * width_new:(x + 1) * width_new]

            # Сохранить часть изображения
            # номер_части = y * grid[0] + x + 1
            new_file_name = f"{num_img}.jpg"
            cv2.imwrite(os.path.join(path_data_out, new_file_name), new_img)
            num_img += 1
            print(num_img)

    for y in range(3):
        for x in range(3):
            # Координаты центра изображения
            # x = int((i + 0.5) * width_new)
            # y = int((j + 0.5) * height_new)

            # Вырезать часть изображения
            new_img = img[int((y + 0.5) * height_new):int((y + 1.5) * height_new), int((x + 0.5) * width_new):int((x + 1.5) * width_new)]
            # print(new_img)
            # Сохранить часть изображения
            # номер_части = y * grid[0] + x + 1
            new_file_name = f"{num_img}.jpg"
            cv2.imwrite(os.path.join(path_data_out, new_file_name), new_img)
            num_img += 1
            print(num_img)


"""Поворот изображений"""
# Пройтись по всем изображениям в папке
for img_name in os.listdir(path_data_in):
    # Загрузить изображение
    img = cv2.imread(os.path.join(path_data_in, img_name))
    # Сохранить часть изображения
    new_file_name = f"{num_img}.jpg"
    cv2.imwrite(os.path.join(path_data_out, new_file_name), img)
    num_img += 1
    print(num_img)

    # поворот на 90
    new_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    # Сохранить часть изображения
    new_file_name = f"{num_img}.jpg"
    cv2.imwrite(os.path.join(path_data_out, new_file_name), new_img)
    num_img += 1
    print(num_img)

    # поворот на 180
    new_img = cv2.rotate(img, cv2.ROTATE_180)
    # Сохранить часть изображения
    new_file_name = f"{num_img}.jpg"
    cv2.imwrite(os.path.join(path_data_out, new_file_name), new_img)
    num_img += 1
    print(num_img)

    # поворот на 270
    new_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # Сохранить часть изображения
    new_file_name = f"{num_img}.jpg"
    cv2.imwrite(os.path.join(path_data_out, new_file_name), new_img)
    num_img += 1
    print(num_img)

"""Отзеркаливание изображений"""
for img_name in os.listdir(path_data_out):
    # Загрузить изображение
    img = cv2.imread(os.path.join(path_data_out, img_name))

    # отзеркаливание изображения
    new_img = cv2.flip(img, 0)

    # Сохранить часть изображения
    new_file_name = f"{num_img}.jpg"
    cv2.imwrite(os.path.join(path_data_out, new_file_name), new_img)
    num_img += 1
    print(num_img)


for img_name in os.listdir(path_data_out):
    # Загрузить изображение
    img = cv2.imread(os.path.join(path_data_out, img_name))

    # попробовать этот вариант
    # new_width = 640  # Измените это значение на желаемую ширину
    # new_height = 480  # Измените это значение на желаемую высоту
    # Определить новый размер
    new_width = 2432
    new_height = 2432

    # Изменить размер изображения
    resized_image = cv2.resize(img, (new_width, new_height))

    # Сохранить измененное изображение
    cv2.imwrite(os.path.join(path_data_out, img_name), resized_image)
