from IPython import display

# print(display.clear_output())

# import ultralytics
#
# print(ultralytics.checks())
#
# import torch
# print(torch.cuda.is_available())

from ultralytics import YOLO
if __name__ == '__main__':
# Load a model
    model = YOLO('yolov8m.pt')  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data='data.yaml', epochs=100, imgsz=1080, device=0, batch=8)
