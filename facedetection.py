import cv2
import os
dataset= "dataset"
name = "dona"

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.mkdir(path)
(width,height)=(260,200)
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)
cam = cv2.VideoCapture(0)
count=1

while count<50:
    print(count)
    _, img = cam.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        faceonly= grayImg [y:y+h , x:x+w]
        resizeimg= cv2.resize(faceonly, (width,height))
        cv2.imwrite("%s/%s.jpg" % (path,count),resizeimg)
        count+=1
    cv2.imshow("FaceDetection",img)
    key = cv2.waitKey(10)
    if key == 27:
        break
print("Image Captured succesfully ")
cam.release()
cv2.destroyAllWindows()

