import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
window=tk.Tk()
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
running=0
reset=0
check=0
def start():
    global reset
    reset=0
    if running==0:
        countfun(59,29)

def reset():
    global reset,check
    reset=1
    check=0
    checkmarks.configure(text=check * "✔")

def countfun(sec,min):
    #print(count
    if min>=0:
        if min>10:
            canvas.itemconfig(timertext, text=f"{min}:{sec}" )
        if sec>10:
            canvas.itemconfig(timertext, text=f"{min}:{sec}")
        if min<10:
            canvas.itemconfig(timertext, text=f"0{min}:{sec}")
        if sec < 10:
            if min < 10:
                canvas.itemconfig(timertext, text=f"0{min}:0{sec}")
            else:
                canvas.itemconfig(timertext, text=f"{min}:0{sec}")
    if min>=0:
        global running,reset,check
        running=1
        if sec==0 and reset==0:
            window.after(1000, countfun, 59,min-1)
        elif sec!=0 and reset==0:
            window.after(1000, countfun, sec-1, min)
        else:
            canvas.itemconfig(timertext, text=f"30:00")
            running=0

    else:
        running=0
        check+=1
        checkmarks.configure(text=check*"✔")



# ---------------------------- UI SETUP ------------------------------- #

window.title("pomodoro app")
window.config(padx=100,pady=50,background=YELLOW)
canvas=tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas1=tk.Canvas(width=200, height=80, background=YELLOW, highlightthickness=0)
img=tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
canvas1.create_text(100,40,text="TIMER",fill=GREEN,font=(FONT_NAME,25,"bold"))
canvas1.grid(row=0,column=1)
timertext=canvas.create_text(100,130,text="30:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
button1=tk.Button(text="start",command=start)
button1.grid(row=2,column=0)
button2=tk.Button(text="reset",command=reset)
button2.grid(row=2,column=2)


checkmarks=tk.Label(text="",font=("",15,"bold"))
checkmarks.configure(background=YELLOW,fg=GREEN)
checkmarks.grid(row=3,column=1)




window.mainloop()