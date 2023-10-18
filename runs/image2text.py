import cv2
import numpy as np
import easyocr
import io


# image = np.array(bytearray(image_file.read()), dtype=np.uint8)
# image = cv2.imdecode(image, cv2.IMREAD_COLOR)

image = cv2.imread('sample.jpg')

reader = easyocr.Reader(['en'])
        
results = reader.readtext(image)

    
detected_text = ""
for (box, text, prob) in results:
    detected_text += text + " "
    print('Detected text: ', detected_text)