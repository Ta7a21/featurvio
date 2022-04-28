import cv2


def read(image_path):
    return cv2.imread(image_path)


def write(image_path, image):
    cv2.imwrite(image_path, image)
