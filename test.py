from ultralytics import YOLO
import argparse
from ultralytics.utils.plotting import Annotator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('-l', '--loc', required=True)
    # parser.add_argument('-m', '--model', required=True)
    args = parser.parse_args()
    model = YOLO('best_xl_latest.pt')

    results = model(['t4.png', 't6.png'], stream=True, save_conf=True,
                    save=True, conf=0.4, save_txt=True, imgsz=640)

    # Process results generator
    for result in results:
        # detection
        print(result.boxes.xyxy)   # box with xyxy format, (N, 4)
        print(result.boxes.xywh)  # box with xywh format, (N, 4)
        # classification
        print(result.probs)     # cls prob, (num_class, )
