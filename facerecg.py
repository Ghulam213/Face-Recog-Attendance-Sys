import face_recognition
import cv2
import time
import pickle
import concurrent.futures


start = time.time()

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
        img_name = "{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))


cam.release()

cv2.destroyAllWindows()

webcam_image = face_recognition.load_image_file('D:\Documents\FRAttendanceSystem\{}'.format(img_name))
webcam_encodings = face_recognition.face_encodings(webcam_image)[0]



with open('pickled_encodings2.pkl', 'rb') as pickle_file:
    new_encodings = pickle.load(pickle_file)

for encoding in new_encodings:
    result = face_recognition.compare_faces([webcam_image], encoding)
    if result[0]:
        print('Present!')
        break
else:
    print('Absent!')

end = time.time()



print('It took {}s for the code to execute!'.format(end-start))