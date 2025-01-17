from tkinter import  *
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
reps = 0
timer_count = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer_count)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    count_down(work_sec)
    if reps % 8 == 0:
        count_down(long_break)
        timer.config(text="LONG BREAK", foreground=PINK)
    elif reps % 2 == 0:
        count_down(short_break)
        timer.config(text="SHORT BREAK", foreground=RED)
    else:
        count_down(work_sec)
        timer.config(text="WORKING", foreground=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count - 1)
    else:
       start_timer()
       marks = ''
       session = math.floor(reps/2)
       for i in range(session):
          marks += '✅'
       check_box.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,  bg=YELLOW)

timer = Label(text="Timer", foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
timer.grid(column=2, row=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomoto)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=3, row=3)

check_box = Label(text="", foreground=GREEN, bg=YELLOW)
check_box.grid(column=2, row=3)


window.mainloop()
