import io
from PIL import Image

def imgToByte(img):
    b = io.BytesIO()
    img.save(b, 'jpeg')
    im_bytes = b.getvalue()
    return im_bytes