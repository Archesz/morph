import cv2 as cv  # Computer vision


def get_kernel(format, size):
    structures = {
        "Rect": cv.MORPH_RECT,
        "Ellipse": cv.MORPH_ELLIPSE,
        "Cross": cv.MORPH_CROSS
    }
    element = structures[format]
    kernel = cv.getStructuringElement(element, size)
    return kernel


def erosion(img, kernel, iterations):
    eroded = cv.erode(img.copy(), kernel, iterations=iterations)
    return eroded

def dilation(img, kernel, iterations):
    dilated = cv.dilate(img.copy(), kernel, iterations=iterations)
    return dilated

def opening(img, kernel, iterations):
    img_opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel, iterations=iterations)
    return img_opening

def closing(img, kernel, iterations):
    closing_img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel, iterations=iterations)
    return closing_img  

def gradient(img, kernel, iterations):
    gradient_img = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel, iterations=iterations)
    return gradient_img

def tophat(img, kernel, iterations):
    tophat_img = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel, iterations=iterations)
    return tophat_img

def applyOperation(img, op, kernel, iterations):
    
    if op == 'Erosão':
        result = erosion(img, kernel, iterations)

    elif op == 'Dilatação':
        result = dilation(img, kernel, iterations)

    elif op == 'Opening':
        result = opening(img, kernel, iterations)

    elif op == 'Closing':
        result = closing(img, kernel, iterations)

    elif op == 'Gradient':
        result = gradient(img, kernel, iterations)

    elif op == 'Tophat':
        result = tophat(img, kernel, iterations)

    return result