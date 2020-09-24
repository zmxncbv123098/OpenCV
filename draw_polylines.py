import cv2
import json
import os
import numpy as np


folder = 'cars/'
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
        with open(os.path.join(folder, filename.split('.')[0] + ".json"), "r") as json_file:
            d = json.load(json_file)
            output = img.copy()
            for polygon in d['shapes']:
                pts = np.array(polygon["points"], np.int32)
                pts = pts.reshape((-1, 1, 2))
                overlay = img.copy()
                alpha = 0.6
                cv2.fillPoly(output, [pts], (0, 255, 0))
                cv2.addWeighted(output, alpha, overlay, 1-alpha, 0, output)
            cv2.imshow("1", output)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


