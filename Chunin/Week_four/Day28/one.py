from tkinter import *
# --------------------------------- CONSTANTS --------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9hdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# --------------------------------- TIMER RESET --------------------------------- #

# --------------------------------- TIMER MECHANISM --------------------------------- #

# --------------------------------- COUNTDOWN MECHANISM --------------------------------- #

# --------------------------------- UI SETUP  --------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=512, height=512, bg=YELLOW, highlightthickness=0)
images_img = PhotoImage(file="images.png")
canvas.create_image(256, 256, image=images_img)
canvas.create_text(256, 256,text="00:00", fill= "black", font=(FONT_NAME, 35, "bold"))
canvas.pack()











window.mainloop()