from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from ttkthemes import ThemedTk

# ======================================Defining Main Window=====================================================
root = ThemedTk(theme='radiance')
root.title('Attendance System')
root.iconbitmap('icon.ico')
root.geometry('800x650')

# defining frames

titleFrame = ttk.Frame(root, width='800', height='50')
titleFrame.pack(side=TOP)

middleFrame = ttk.Frame(root, width='800', height='100')
middleFrame.place(x=0, y=50)

canvasFrame = ttk.Frame(root, width='800', height='395')
canvasFrame.place(x=0, y=150)

bottomFrame = ttk.Frame(root, width='800', height='100')
bottomFrame.pack(side=BOTTOM)

# ---------------------------------------------- in top frame-------------------------------------------------

titleName = ttk.Label(titleFrame, text='ATTENDANCE THROUGH FACIAL RECOGNITION',
                      font=('Times New Roman', 20, 'bold'))
titleName.place(x=65, y=20)

# ----------------------------------------- in middle frame---------------------------------------------------

inputName = ttk.Label(middleFrame, text='Enter Name:',
                      font=('Times New Roman', 13, 'bold'))
inputName.place(x=160, y=30)

name_display = ttk.Entry(middleFrame, width=40, font=('arial', 11))
name_display.place(x=280, y=30)

# making a drop down menu of courses
courseVar = StringVar()
courseVar.set('Choose Course')

courseName = ttk.Label(middleFrame, text='Course:',
                       font=('Times New Roman', 13, 'bold'))
courseName.place(x=160, y=70)

course_list = ['Calculus', 'Physics', 'Fundamentals of Programming', 'English', 'Discrete Maths', 'Islamiat']
course_menu = ttk.OptionMenu(middleFrame, courseVar, *course_list, )
course_menu.place(x=280, y=70)

# --------------------------------------------- in canvas Frame--------------------------------------------------

imageCanvas = Canvas(canvasFrame, width=500, height=350, borderwidth=10, bg='grey')
imageCanvas.place(x=150, y=10)

# adding image just to show functioning
image = ImageTk.PhotoImage(Image.open('canvas-img.png'))
imageCanvas.create_image(140, 50, image=image, anchor=NW)

# ========================================Defining Buttons=========================================
# in bottomFrame
# making a status bar

statusbar = ttk.Label(bottomFrame, text='Enter Credentials...', font=('calibri(body)', 10, 'italic')
                   , relief=SUNKEN, anchor=W)
statusbar.grid(row=2, column=0, columnspan=6, sticky=W + E)


# defining buttons functionality

def markAttendence():
    global student_name
    student_name = name_display.get()
    statusbar['text'] = 'Marking Attendence'


def reset():
    name_display.delete(0, END)
    courseVar.set('Choose Course')
    student_name = ''
    statusbar['text'] = 'Enter Credentials'


# making buttons
markBtn = ttk.Button(bottomFrame, text='Mark Attendence', command=lambda: markAttendence())
markBtn.grid(row=0, column=1, padx=80, pady=20)

resetBtn = ttk.Button(bottomFrame, text='Reset', command=lambda: reset())
resetBtn.grid(row=0, column=3, padx=50, pady=20)

exitBtn = ttk.Button(bottomFrame, text='EXIT', command=root.quit)
exitBtn.grid(row=0, column=5, padx=80, pady=20)

root.mainloop()
