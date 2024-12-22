import cv2

def resize_image(image, max_width):
    height, width = image.shape[:2]
    if width > max_width:
        scaling_factor = max_width / float(width)
        image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread('D:/45-Days-Challege-JS-Python/ieee-conference.JPG')

resized_image = resize_image(image, 1080)

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

for (x, y, w, h) in faces:
    cv2.rectangle(resized_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Faces detected', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
