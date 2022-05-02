import numpy as np # Math manipulation
import cv2 # Computer vision
import matplotlib.pyplot as plt # View
import skimage.io as io # Image manipulation
from PIL import Image, ImageOps

def watershed_with_markers(im):
    ret, thresh = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # Definindo Elemento estruturante
    kernel = np.ones((3, 3), np.uint8)
    first_operation = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    sure_bg = cv2.dilate(first_operation, kernel, iterations=3)

    dist_transform = cv2.distanceTransform(first_operation, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(
        dist_transform, 0.7 * dist_transform.max(), 255, 0)

    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    markers = cv2.watershed(im, markers)
    # im[markers == -1] = [255, 0, 0]

    return markers