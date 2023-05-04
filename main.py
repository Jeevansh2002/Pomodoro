from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
X = 230
Y = 350
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global REPS
    window.after_cancel(timer)
    REPS = 0
    canvas.itemconfig(canvas_text,text="00:00")
    label.config(text="Timer",fg=GREEN,font=(FONT_NAME,30,"bold"))
    label.place(x=180,y=10)
    tick_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global REPS
    global X
    global Y
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    if count == 0:
        start_timer()
        if REPS % 2 == 0 and count == 0:
            tick_label.config(text=f"✓",bg=YELLOW,fg=GREEN)
            tick_label.place(x=X,y=Y)
            X += 5


def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        label.config(text="It's a long break",font=(FONT_NAME,20,"bold"),fg="black")
        label.place(x=140,y=10)
        count_down(20*60)
    elif REPS % 2 == 0:
        label.config(text="It's a short-break",font=(FONT_NAME,20,"bold"),fg="black")
        label.place(x=140,y=10)
        count_down(5*60)
    else:
        label.config(text="It's study time",font=(FONT_NAME,20,"bold",),fg="black")
        label.place(x=140,y=10)
        count_down(25*60)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=500,height=400)
window.title("Pomodoro")
window.config(bg=YELLOW)

#Canvas
canvas = Canvas(width=300,height=300,highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(150,170,image=photo)
canvas_text = canvas.create_text(150, 190, text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.config(bg=YELLOW)
canvas.place(x=100,y=10)

#Tools
label = Label(text="Timer",fg=GREEN, font=(FONT_NAME,30,"bold"),bg=YELLOW)
label.place(x=180,y=10)

start_button = Button(text="Start",bg=GREEN,fg="white",font=(FONT_NAME,10,"bold"),command=start_timer)
start_button.place(x=130,y=320)

tick_label = Label(bg=YELLOW,fg=GREEN)
tick_label.place(x=240,y=350)

reset_button = Button(text="Reset",bg=GREEN,fg="white",font=(FONT_NAME,10,"bold"),command=reset)
reset_button.place(x=320,y=320)





window.mainloop()
