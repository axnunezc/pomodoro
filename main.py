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
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global TIMER
    global REPS
    
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER")
    check_label.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    
    work = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    
    if REPS % 8 == 0:
        time = long_break
        timer_label.config(text="BREAK", fg=RED)
    elif REPS % 2 == 0:
        time = short_break
        timer_label.config(text="BREAK", fg=PINK)
    else:
        time = work
        timer_label.config(text="WORK")
    
    countdown(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global TIMER
    
    minutes = math.floor(count / 60)
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
timer_label.grid(column=1, row=0)

check_label = Label(bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()