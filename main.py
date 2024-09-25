import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        label1.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        label1.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        label1.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_txt, text= f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count -1)
    else:
        start_timer()
        marks = ""
        work_sess = math.floor(reps/2)
        for _ in range(work_sess):
            marks += "✔️"
        label2.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= img)
timer_txt = canvas.create_text(100,130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)



label1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label1.grid(row=0, column=1)


button1 = Button(text="Start", command=start_timer)
button1.grid(row= 2,column=0)

button2 = Button(text="Reset", command=reset)
button2.grid(row= 2,column=2)

label2 = Label(fg=GREEN, bg= YELLOW)
label2.grid(row=3, column=1)


window.mainloop()