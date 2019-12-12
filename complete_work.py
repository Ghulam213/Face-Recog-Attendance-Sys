
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
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle
import time
import cv2
from tkinter import messagebox



#
# ##----------------------------------------making pkl file of encodings-------------------------------------------
# encodings = face_recognition.face_recognition_cli.scan_known_people('C:\\Users\\addbi\\Desktop\\facerecognitions\\')
#
# pickle_out = open('encodings.pkl', 'wb')
# pickle.dump(encodings, pickle_out)
# pickle_out.close()





# ======================================Defining Main Window=====================================================

root = ThemedTk(theme='awdark')
root.title('Attendance System')
#root.iconbitmap('icon.ico')
root.geometry('1280x620')
# style = ThemedStyle(root)
# style.set_theme('smog')
root.configure(background='light grey')

style= ttk.Style()
style.theme_use('clam')
# adding picture
# img = ImageTk.PhotoImage(Image.open("C:\\Users\\addbi\\Desktop\\a"))

# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")


# defining frames

titleFrame = Frame(root, width='900', height='100')
titleFrame.pack(side=TOP)
top_style =ThemedStyle(titleFrame)
top_style.set_theme('smog')

middleFrame = Frame(root, width='730', height='200')
middleFrame.place(x=680, y=110)
middle_style =ThemedStyle(middleFrame)
middle_style.set_theme('smog')

picFrame = Frame(root, width='700', height='500')
picFrame.place(x=40, y=110)
lmain = ttk.Label(picFrame)
lmain.grid()

bottomFrame = Frame(root, width='730', height='100')
bottomFrame.place(x=680, y=450)

statusFrame = Frame(root, width='1280', height='10')
statusFrame.place(x=0, y=600)

timerFrame = Frame(root, width='730', height='100')
timerFrame.place(x=680, y=300)


#--------------------------adding a image------------------------------------------------------------------------

load = Image.open("images.png")
render = ImageTk.PhotoImage(load)

# labels can be text or images
img = Label(root, image=render)
img.image = render
img.place(x=200, y=150)


# -------------------------------------------in timer frame----------------------------------------------------

time_lb = ttk.Label(timerFrame, text='Time Remaining: ',
                    font=('Times New Roman', 15, 'bold'))
time_lb.place(x=60, y=30)
w = Canvas(timerFrame, width=450, height=450)
w.place(x=220, y=20)
w.configure(background = 'red')
run = True
s = 59
m = 9
h = 0


def Run():
    global run, s, m, h

    # Delete old text
    w.delete('all')
    # Add new text
    w.create_text(
        [100, 25], anchor=CENTER, text="%s:%s:%s" % (h, m, s), font=("Consolas", 25)
    )

    # s+=1

    if m == 0 and s == 0:
        run = False
        return
    elif s == 0:
        m -= 1;
        s = 59
    s -= 1
    # After 1 second, call Run again (start an infinite recursive loop)
    timerFrame.after(1000, Run)


def timer():
    if run:
        timerFrame.after(1, Run)
    else:
        markBtn = Button(bottomFrame, text='Mark Attendence',  state=DISABLED)
        markBtn.grid(row=0, column=1, padx=40, pady=20)
    #root.quit()


timer()


# ---------------------------------------------- in top frame-------------------------------------------------

titleName = ttk.Label(titleFrame, text='ATTENDANCE THROUGH FACIAL RECOGNITION',
                      font=('Times New Roman', 15, 'bold'))
titleName.place(x=100, y=20)
titleFrame.configure(background='light grey')


# ----------------------------------------- in middle frame---------------------------------------------------

#-----------------------taking the user name
inputName = ttk.Label(middleFrame, text='Enter Name:',
                      font=('Times New Roman', 13, 'bold'))
inputName.place(x=60, y=30)

name_display = ttk.Entry(middleFrame, width=45, font=('arial', 11))
name_display.place(x=180, y=30)

# making a drop down menu of courses
courseVar = StringVar()
courseVar.set('Choose Course')

courseName = ttk.Label(middleFrame, text='Course:',
                       font=('Times New Roman', 13, 'bold'))
courseName.place(x=60, y=70)

course_list = ['Choose Course', 'Calculus', 'Physics', 'Fundamentals of Programming', 'English', 'Discrete Maths',
               'Islamiat']
course_menu = ttk.OptionMenu(middleFrame, courseVar, *course_list)
course_menu.place(x=180, y=70)






# ========================================Defining status bar=========================================
# in bottomFrame
# making a status bar

statusbar = ttk.Label(statusFrame, text='Enter Credentials...', font=('calibri(body)', 10, 'italic')
                      , relief=SUNKEN, anchor=W)
statusbar.grid(row=0, column=0, sticky=W + E)
statusbar.config(width='1280')

statusbar.configure(background='lawn green')




#----------------------------------------defining the main face recognition function-------------------------------
def main():

    pickle_in = open('encodings.pkl','rb')
    pickled_encodings = list(pickle.load(pickle_in))
    pickle_in.close()

    # taking the user entered name from above gui
    global student_name
    student_name = name_display.get()
    statusbar['text'] = 'Taking Live Image...'

    if student_name in pickled_encodings[0]:
        index_of_name_encodings = pickled_encodings[0].index(student_name)
    else:
        messagebox.showinfo('Error', 'The system could not find your name reset and try again')



#capturing image from webcam
    cam = cv2.VideoCapture(0)
    # video_stream()
    cv2.namedWindow("test")
    start = time.time()

    img_counter = 0

    while int(time.time() - start) != 5:
        global frame
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        #cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        #img = Image.fromarray(cv2image)
        if not ret:
            break
        k = cv2.waitKey(1)
    global img_name
    img_name = "{}.jpg".format('live')
    cv2.imwrite(img_name, frame)
    #print("{} written!".format(img_name))
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations)>1:
        messagebox.showinfo('Error', 'The system could not take a clear picture of a single person press reset button')

    else:

        biden_encoding_unknown_image = face_recognition.face_encodings(frame)[0]



    cam.release()

    # taking the index of the particular person entering name

    # if student_name in pickled_encodings[0]:
    #     index_of_name_encodings = pickled_encodings[0].index(student_name)
    # else:
    #     messagebox.showinfo('Error', 'The system could not find your name reset and try again')

    # taking out the particular image and find its encoding and comaring

    image_encoding = pickled_encodings[1][index_of_name_encodings]

    # comparing the results

    results = face_recognition.compare_faces([image_encoding], biden_encoding_unknown_image,)
    print(results)




    if True in results and student_name in pickled_encodings[0]:
        messagebox.showinfo('Face recognitions result', 'your attendance have been marked')
        statusbar['text']= 'showing results'
    elif False in results:
        messagebox.showinfo('Face recognitions result', 'your attendance have not been marked')




#---------------------------------------reset function--------------------------------
def reset():
    name_display.delete(0, END)
    courseVar.set('Choose Course')
    student_name = ''
    statusbar['text'] = 'Enter Credentials'
    # lmain.grid_forget()













#----------------------------------DEFINING BUTTONS AFTER THEIR FUCTIONS---------------------------------------


# making buttons
markBtn = ttk.Button(bottomFrame, text='Mark Attendence', command=lambda: main(),)
markBtn.grid(row=0, column=1, padx=40, pady=20)

resetBtn = ttk.Button(bottomFrame, text='Reset', command=lambda: reset())
resetBtn.grid(row=0, column=3, padx=30, pady=20)

exitBtn = ttk.Button(bottomFrame, text='EXIT', command=root.quit)
exitBtn.grid(row=0, column=5, padx=40, pady=20)




root.mainloop()