import cv2
num=0
videoWebcam = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier("cat.xml")
while True:

    valeurRetour, imageWebcam = videoWebcam.read()
    #gray = imageWebcam
    gray = cv2.cvtColor(imageWebcam, cv2.COLOR_BGR2GRAY)
    faces = face_model.detectMultiScale(gray)
    visage=False
    for face in faces:
        cv2.rectangle(gray, (face[0], face[1]), (face[0] + face[2], face[0] + face[3]), (255, 0, 0), 3)
        out = cv2.imwrite('/var/www/html/uploads/%s.png' % (num), imageWebcam)
        num=num+1

videoWebcam.release()
cv2.destroyAllWindows()
