from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER")
    check_mark.config(text="")
    global reps, timer
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, timer
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    reps += 1

    if reps % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        countdown(short_break_sec)
    else:
        title_label.config(text="WORK", fg=GREEN)
        countdown(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:

        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark.config(text=math.floor(reps/2)*"✔")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)



start_button = Button(width=5, text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(width=5, text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font=("Arial", 15))
check_mark.grid(column=1, row=3)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", 40, "bold"))
title_label.grid(column=1, row=0)
title_label.config(pady=10)







window.mainloop()





