from pytesseract import pytesseract
import cv2
import imutils
#global rotated_image
pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("test.jpg")

def Detection(img):
    #check letters
    detected_letter = pytesseract.image_to_string(img , config="--psm 10")
    if detected_letter[0] in "HSUsu":
        #print("found", detected_letter)
        return detected_letter[0]
    else:
        return "no"
def rotation90():
    for i in range(4):
        rotated_image = imutils.rotate(img, angle=i*90)
        if Detection(rotated_image) in "HSUsu":
            #print(Detection(rotated_image))
            return Detection(rotated_image)
            break
        else:
            continue
def rotation(img):
    if (rotation90() in "HSUsu"):
        print(rotation90())
    else:
        for i in range(180):
            rotated_image = imutils.rotate(img, angle=i*2)
            if Detection(rotated_image) in "HSUsu":
                print(Detection(rotated_image))
                break
            else:
                continue
if Detection(img) in "HSUsu":
    print("detected  " + Detection(img))
elif Detection(img)=="no":
    rotation(img)
    
