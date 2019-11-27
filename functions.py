def student_name():
    name = input('Enter your name: ')
    return name


def student():
    student = student_name(name)
    image = face_recognition.load_image_file('D:\Documents\FRAttendanceSystem\images\{}.jpg'.format(student))
    image_encodings = face_recognition.face_encodings(image)[0]
    return image_encodings
