import xml.etree.ElementTree as ET
import os
def parse_xml(filename):
  tree = ET.parse(filename)
  root = tree.getroot()

  # Извлечь текст элемента filename
  filename_text = root.find("filename").text
  # print(filename_text)
  # Извлечь значения width и height
  width = int(root.find("size").find("width").text)
  height = int(root.find("size").find("height").text)

  # Инициализировать пустой список для хранения объектов
  objects = []

  # Обработать каждый тег object
  for obj in root.findall("object"):
    # Извлечь текст элемента name
    name_text = obj.find("name").text

    # Извлечь значения xmin, ymin, xmax, ymax из bndbox
    bndbox = obj.find("bndbox")
    xmin = int(bndbox.find("xmin").text)
    ymin = int(bndbox.find("ymin").text)
    xmax = int(bndbox.find("xmax").text)
    ymax = int(bndbox.find("ymax").text)

    # Создать словарь для хранения данных объекта
    object_data = {
        "name": name_text,
        "bndbox": {
            "xmin": xmin,
            "ymin": ymin,
            "xmax": xmax,
            "ymax": ymax
        }
    }

    # Добавить словарь данных объекта в список
    objects.append(object_data)

  # Создать словарь для хранения всех извлеченных данных
  data = {
      "filename": filename_text,
      "width": width,
      "height": height,
      "objects": objects
  }

  return data


#  путь к папке с изображениями
path_data_in = 'C:/Users/kimsl/VKR/dataset_prepro_yolo/Annotations'
path_data_out = 'C:/Users/kimsl/VKR/dataset_prepro_yolo/annotations_txt'
#
for filemame in os.listdir(path_data_in):

    data = parse_xml(os.path.join(path_data_in, filemame))

    # print(f"Filename: {data['filename']}")
    # print(f"Width: {data['width']}")
    # print(f"Height: {data['height']}")
    #
    # for obj in data["objects"]:
    #     print(f"Name: {obj['name']}")
    #     print(f"Bndbox: {obj['bndbox']}")

    with open(f"{path_data_out}/{data['filename'][:-4]}.txt", "w") as txt_file:
        # Записать в файл информацию о каждом объекте
        for obj in data["objects"]:
            if obj['name'] == 'missing_hole':
                defect = 0
            if obj['name'] == 'mouse_bite':
                defect = 1
            if obj['name'] == 'open_circuit':
                defect = 2
            if obj['name'] == 'short':
                defect = 3
            if obj['name'] == 'spur':
                defect = 4
            if obj['name'] == 'spurious_copper':
                defect = 5
            x_centr = ((obj['bndbox']['xmin'] + obj['bndbox']['xmax'])/2)/data['width']
            y_centr = ((obj['bndbox']['ymin'] + obj['bndbox']['ymax'])/2)/data['height']
            width = (obj['bndbox']['xmax'] - obj['bndbox']['xmin'])/data['width']
            height = (obj['bndbox']['ymax'] - obj['bndbox']['ymin'])/data['height']
            # txt_file.write(f"{obj['name']} {obj['bndbox']['xmin']} {obj['bndbox']['ymin']} {obj['bndbox']['xmax']} {obj['bndbox']['ymax']}\n")
            txt_file.write(f"{defect} {x_centr} {y_centr} {width} {height}\n")





# import xml.etree.ElementTree as ET
#
# tree = ET.parse('01_missing_hole_01.xml')
# root = tree.getroot()
#
# # for name in root.findall('filename'):
# #     print(name.text)
# #
# # for size in root.findall('filename'):
# #
# #     print(size.text)
# width = 0
# height = 0
# for elem in root:
#     if elem.tag == 'filename':
#         filename = elem.text
#         # print(elem.text)
#
#     if elem.tag == 'size':
#         for size in elem:
#             if size.tag == 'width':
#                 width = size.text
#                 # print(width)
#             if size.tag == 'height':
#                 height = size.text
#                 # print(size.text)
#
#     if elem.tag == 'object':
#
#         for obj in elem:
#
#             if obj.tag == 'name':
#                 defect_name = obj.text
#                 if obj.text == 'missing_hole':
#                     defect = 0
#
#                 if obj.text == 'mouse_bite':
#                     defect = 1
#
#                 if obj.text == 'open_circuit':
#                     defect = 2
#
#                 if obj.text == 'short':
#                     defect = 3
#
#                 if obj.text == 'spur':
#                     defect = 4
#
#                 if obj.text == 'spurious_copper':
#                     defect = 5
#                 # print(obj.text)
#
#
#             if obj.tag == 'bndbox':
#                 for coord in obj:
#                     if coord.tag == 'xmin':
#                         xmin = coord.text
#                         print(xmin)
#
#                         # print(coord.text)
#
#                     if coord.tag == 'ymin':
#                         ymin = coord.text
#                         # print(coord.text)
#
#                     if coord.tag == 'xmax':
#                         xmax = coord.text
#                         # print(coord.text)
#
#                     if coord.tag == 'ymax':
#                         ymax = coord.text
#                         # print(coord.text)
#             # print(width)
#             # print(xmin)
#             # print(xmax)
#
#             # x_centr = ((xmin + xmax)/2)/width
#             # y_centr = ((ymin + ymax)/2)/height
#             # print(x_centr)
#

