
import os
from PIL import Image
import cv2
from os import listdir
import face_recognition
import pickle
from PIL import Image
from face_recognition.face_recognition_cli import image_files_in_folder
import cv2
import time

# encodings = face_recognition.face_recognition_cli.scan_known_people('C:\\Users\\addbi\\Desktop\\facerecognitions\\')
#
#
# pickle_out = open('encodings.pkl','wb')
# pickle.dump(encodings,pickle_out)
# pickle_out.close()

def main():

    pickle_in = open('encodings.pkl','rb')
    pickled_encodings = list(pickle.load(pickle_in))
    pickle_in.close()



    # asking name
    user_name = input('Who are you? ')
    # taking webcam biometric encoding
    print('look into the camera')
    # taking webcam input
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    cv2.imshow('a', frame)
    rgb_frame = frame[:, :, ::-1]
    biden_encoding_unknown_image = face_recognition.face_encodings(frame)[0]

    # taking the index of the particular person entering name

    if user_name in pickled_encodings[0]:
        index_of_name_encodings = pickled_encodings[0].index(user_name)
    else:
        print('name incorrect')

    # taking out the particular image and find its encoding and comaring

    image_encoding = pickled_encodings[1][index_of_name_encodings]

    # comparing the results

    results = face_recognition.compare_faces([image_encoding], biden_encoding_unknown_image,)
    print(results)

    # now checking both

    if True in results and user_name in pickled_encodings[0]:
        print('Your attendance have been marked')
    elif False in results:
        print()
n=0
while n<24:
    start = time.time()
    main()
    end = time.time()
    n+=1
    print(end-start)


