import face_recognition
import time
import pickle


start = time.time()

infile = open('D:\Documents\FRAttendanceSystem\\pickled_encodings','rb')
new_encodings = pickle.load(infile)
infile.close()

def student_encodings(name):
    image = face_recognition.load_image_file('D:\Documents\FRAttendanceSystem\images\{}.jpg.'.format(name))
    image_encodings = face_recognition.face_encodings(image)[0]
    return face_encodings


for encoding in pickled_encodings:
    student = student_encodings('Abdullah Zubair')
    result = face_recognition.compare_faces([student], pickled_encodings)
    if result[0]:
        print('Present in class!')
        break
    else:
        continue
else:
    print('Absent!')

end = time.time()

print('It took {}s for the code to execute!'.format(end-start))