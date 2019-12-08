import face_recognition
import cv2
import time

start = time.time()

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")


img_counter = 0

name = 'Ghulam Muhammad'

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

webcam_image = face_recognition.load_image_file('{}'.format(img_name))
resized = cv2.resize(webcam_image, (1443,1987), interpolation = cv2.INTER_AREA)


image = face_recognition.load_image_file('D:\Documents\FRAttendanceSystem\images\\'+name+'.jpg')
resized2 = cv2.resize(image, (1443,1987), interpolation = cv2.INTER_AREA)


result = face_recognition.compare_faces(resized, resized2)
print(result)

if result[0].all():
    print('Present!')
else:
    print('Absent!')    

end = time.time()


print('It took {}s for the code to execute!'.format(end-start))
