from tkinter import *
import math
from playsound import playsound

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
def reset_timer():
    window.after_cancel(timer)
    playsound("Untitled Project-Benjamin-v8.mp3")
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="Timer")
    check_lbl.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_timer_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    print(reps)

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_timer_sec)
        playsound("Untitled Project-Benjamin-v5.mp3")

    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        playsound("Untitled Project-Benjamin-v1.mp3")

    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break)
        playsound("Untitled Project-Benjamin-v8.mp3")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)  ##after loop in every 1 sec
    else:
        marks = ""
        start_timer()
        reps_count = math.floor(reps / 2)
        for i in range(reps_count):
            marks += "✔"
            check_lbl.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("tomato")
window.config(padx=100, pady=50, bg=YELLOW)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=202, height=230, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1)
canvas.create_image(101, 112, image=image)
timer_text = canvas.create_text(104, 138, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")

timer_label = Label(text="Timer", font=(FONT_NAME, 38, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_btn = Button(text="Start", activeforeground="green", activebackground="white", bg=YELLOW, highlightthickness=0,
                   command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", activebackground="white", activeforeground="red", bg=YELLOW, highlightthickness=0,
                   command=reset_timer)
reset_btn.grid(row=2, column=2)

check_lbl = Label(text="", bg=YELLOW, fg="green")
check_lbl.grid(row=3, column=1)

window.mainloop()
