from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from ttkthemes import ThemedTk
import time
import cv2

# ======================================Defining Main Window=====================================================
root = ThemedTk(theme='radiance')
root.title('Attendance System')
root.iconbitmap('icon.ico')
root.geometry('1280x620')

# defining frames

titleFrame = Frame(root, width='900', height='100')
titleFrame.pack(side=TOP)

middleFrame = Frame(root, width='730', height='200')
middleFrame.place(x=680, y=110)

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
# -------------------------------------------in timer frame----------------------------------------------------

time_lb = ttk.Label(timerFrame, text='Time Remaining: ',
                    font=('Times New Roman', 15, 'bold'))
time_lb.place(x=60, y=30)
w = Canvas(timerFrame, width=450, height=450)
w.place(x=220, y=20)

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
                      font=('Times New Roman', 20, 'bold'))
titleName.place(x=95, y=20)

# ----------------------------------------- in middle frame---------------------------------------------------


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

# ========================================Defining Buttons=========================================
# in bottomFrame
# making a status bar

statusbar = ttk.Label(statusFrame, text='Enter Credentials...', font=('calibri(body)', 10, 'italic')
                      , relief=SUNKEN, anchor=W)
statusbar.grid(row=0, column=0, sticky=W + E)
statusbar.config(width='1280')


# defining buttons functionality


def markAttendence():
    global student_name
    student_name = name_display.get()
    statusbar['text'] = 'Taking Live Image...'
    # global cam
    cam = cv2.VideoCapture(0)
    # video_stream()
    cv2.namedWindow("test")
    start = time.time()

    img_counter = 0

    while int(time.time() - start) != 5:
        global frame
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        if not ret:
            break
        k = cv2.waitKey(1)
    global img_name
    img_name = "{}.jpg".format('live')
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))

    cam.release()
    cv2.destroyAllWindows()

    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    statusbar['text'] = 'Validating Data...'


def reset():
    name_display.delete(0, END)
    courseVar.set('Choose Course')
    student_name = ''
    statusbar['text'] = 'Enter Credentials'
    # lmain.grid_forget()


# making buttons
markBtn = ttk.Button(bottomFrame, text='Mark Attendence', command=lambda: markAttendence())
markBtn.grid(row=0, column=1, padx=40, pady=20)

resetBtn = ttk.Button(bottomFrame, text='Reset', command=lambda: reset())
resetBtn.grid(row=0, column=3, padx=30, pady=20)

exitBtn = ttk.Button(bottomFrame, text='EXIT', command=root.quit)
exitBtn.grid(row=0, column=5, padx=40, pady=20)

root.mainloop()
