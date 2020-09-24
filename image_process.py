# take an image, rotate it 180 degrees, crop by N px from left&right

import cv2
import os


def view_image(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop_left_right(image, px):  # !! n < width
    cropped = image[0:height, px:width - px]
    return cropped


def rotate180(image):
    (h, w, d) = image.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 180, 1)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated


folder = 'images/'
os.makedirs('output', exist_ok=True)
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
        rot = rotate180(img)
        height, width, channels = img.shape
        while True:
            # n = 200  # (un)comment this for specific crop
            n = int(input())
            try:
                crop = crop_left_right(rot, n)
                cv2.imwrite("output/OUT" + filename, crop)
                break
            except cv2.error:
                print("N is greater than width, try again!")
