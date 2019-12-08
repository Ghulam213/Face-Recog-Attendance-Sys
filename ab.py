import face_recognition
import pickle
from face_recognition.face_recognition_cli import image_files_in_folder


encodings = face_recognition.face_recognition_cli.scan_known_people('images\\')
pickle_out = open('encodings.pkl', 'wb')
pickle.dump(encodings, pickle_out)
pickle_out.close()


