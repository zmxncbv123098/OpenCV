import cv2
import json
import os


folder = 'planes/'
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
        with open(os.path.join(folder, filename.split('.')[0] + ".json"), "r") as jsn_file:
            d = json.load(jsn_file)
            output = img.copy()
            for rectangle in d["shapes"]:
                coordinates = rectangle["points"]
                cv2.rectangle(output, (int(coordinates[0][0]), int(coordinates[0][1])), (int(coordinates[1][0]), int(coordinates[1][1])), (0, 255, 255), 5)
            cv2.imshow("1", output)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
