import torch
import numpy as np
import cv2
import time
import plac

@plac.opt('argument', 'some argument', type=str)
def main(argument=None):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    img = cv2.imread('../images/zidane.jpg')

    for i in range(200):
        t0 = time.time()
        results = model(img)
        t1 = time.time() - t0
        print(t1)
        print(results.pred)


if __name__ == '__main__':
    plac.call(main)
