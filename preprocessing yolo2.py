import os
import shutil
import re
import random

images_dir = 'C:/Users/kimsl/VKR/dataset_prepro_yolo/images'
annotations_dir = 'C:/Users/kimsl/VKR/dataset_prepro_yolo/annotations_txt'

images_dir1 = 'C:/Users/kimsl/VKR/dataset_prepro_yolo/images1'
annotations_dir1 = 'C:/Users/kimsl/VKR/dataset_prepro_yolo/annotations_txt1'
train_images_dir = os.path.join(images_dir1, "train")
train_annotations_dir = os.path.join(annotations_dir1, "train")

test_images_dir = os.path.join(images_dir1, "test")
test_annotations_dir = os.path.join(annotations_dir1, "test")

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_annotations_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_annotations_dir, exist_ok=True)

image_filenames = os.listdir(images_dir)
# annotation_filenames = os.listdir(annotations_dir)

train_size = 0.8  # 80% данных для обучения
test_size = 0.2  # 20% данных для тестирования

num_train_samples = int(len(image_filenames) * train_size)
num_test_samples = len(image_filenames) - num_train_samples

random.shuffle(image_filenames)

train_image_filenames = image_filenames[:num_train_samples]
test_image_filenames = image_filenames[num_train_samples:]

for filename in train_image_filenames:
    # Извлеките имя файла без расширения
    # base_filename = re.sub(r"\.[^.]+$", "", filename)
    base_filename = filename[:-4]

    print(filename)
    # Переместите файл изображения
    shutil.move(os.path.join(images_dir, filename), os.path.join(train_images_dir, filename))

    # Переместите файл аннотации
    annotation_filename = base_filename + ".txt"
    print(annotation_filename)
    shutil.move(os.path.join(annotations_dir, annotation_filename), os.path.join(train_annotations_dir, annotation_filename))

for filename in test_image_filenames:
    # Извлеките имя файла без расширения
    # base_filename = re.sub(r"\.[^.]+$", "", filename)
    base_filename = filename[:-4]

    # Переместите файл изображения
    shutil.move(os.path.join(images_dir, filename), os.path.join(test_images_dir, filename))

    # Переместите файл аннотации
    annotation_filename = base_filename + ".txt"
    shutil.move(os.path.join(annotations_dir, annotation_filename), os.path.join(test_annotations_dir, annotation_filename))



#
# if len(image_filenames) != len(annotation_filenames):
#     raise ValueError("Количество имен файлов изображений не совпадает с количеством имен файлов аннотаций!")
#
# random.shuffle(image_filenames)
# random.shuffle(annotation_filenames)
#
#
# train_size = 0.8  # 80% данных для обучения
# test_size = 0.2  # 20% данных для тестирования
#
# num_train_samples = int(len(image_filenames) * train_size)
# num_test_samples = len(image_filenames) - num_train_samples
#
#
# train_image_filenames = image_filenames[:num_train_samples]
# train_annotation_filenames = annotation_filenames[:num_train_samples]
#
# test_image_filenames = image_filenames[num_train_samples:]
# test_annotation_filenames = annotation_filenames[num_train_samples:]
#
#
