from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO("yolov8x.pt")

    model.train(data="data_custom.yaml", batch=2, imgsz=640,
                epochs=100, workers=1)
