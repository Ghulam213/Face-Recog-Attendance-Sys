import face_recognition
import cv2
from functions import student_name

import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

face = face_recognition.load_image_file('D:\Documents\FRAttendanceSystem\{}'.format(img_name))
face_encodings = face_recognition.face_encodings(img_name)[0]

rakshak = face_recognition.load_image_file('D:\Documents\FRAttendanceSystem\images\Raja Rakshak.jpg')
encodings = face_recognition.face_encodings(rakshak)[0]


results = face_recognition.compare_faces([face_encodings], encodings)

if results[0]:
    print('ok')
else:
    print('okkkk')

