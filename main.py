from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 #25
SHORT_BREAK_MIN = 5 #5
LONG_BREAK_MIN = 20 #20
REPS = 0 #0
TIMER = None
# ----------------------------------------------------------------------- #
class Pomodoro(Tk):
    """The Pomodoro app is a time management tool based on the Pomodoro Technique, 
    which helps users focus on work and take regular breaks. """
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.config(padx=100, pady=50, bg=YELLOW)
        self.resizable(0,0)
        self.time_left = WORK_MIN * 60
        self.long_brake = LONG_BREAK_MIN * 60
        self.short_brake = SHORT_BREAK_MIN * 60
        self.timer_running = False
        self.layout()
        

    def canvas_for_image(self):
        """This method creates the canvas for the app. 
        Here the image and timer text are created and placed using the grid system."""
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_imf = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_imf)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
        self.canvas.grid(row=1,column=1)
            

    def timer_text_label(self):
        """This method creates the label for the timer."""
        self.text_label = Label(text="Timer",bg=YELLOW,fg=GREEN ,font=(FONT_NAME, 20, "bold"))
        self.text_label.grid(row=0, column=1)


    def check_mark_label(self):
        """This method creates the label for the check mark."""
        self.check_mark = Label(bg=YELLOW,fg=GREEN ,font=(FONT_NAME, 15, "bold"), padx=25, pady=25)
        self.check_mark.grid(row=4, column=1)


    def start_button(self):
        """This method creates 'Start' button."""
        self.start_t_button = Button(text="Start",fg=GREEN ,font=(FONT_NAME, 13, "bold"), padx=2, pady=2, command=self.start_timer)
        self.start_t_button.grid(row=4, column=0)


    def reset_button(self):
        """This method creates 'Reset' button."""
        self.reset_button = Button(text="Reset",fg=GREEN ,font=(FONT_NAME, 13, "bold"), padx=2, pady=2, command=self.reset_timer)
        self.reset_button.grid(row=4, column=2)
        

    def count_down(self, count):
        """Count down logic method"""
        self.minutes_count = math.floor(count / 60)
        self.seconds_count = count % 60
        self.formatted_count = f"{self.minutes_count:02}:{self.seconds_count:02}"
        self.canvas.itemconfig(self.timer_text, text=self.formatted_count)
        
        if count > 0:
            global TIMER
            TIMER = self.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            mark = ""
            work_sessions = math.floor(REPS/2)
            for _ in range(work_sessions):
                mark += "✔"
            self.check_mark.config(text=mark)



    def reset_timer(self):
        """Resets the timer when called 'used as command in reset button'.
        Resets REPS as well as re-activates the Start 'Button'."""
        self.after_cancel(TIMER)
        self.check_mark.config(text="")
        self.text_label.config(text="Timer")
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.timer_running = False
        self.start_t_button.config(state="normal")
        global REPS
        REPS = 0

    def start_timer(self):
        """Starts the timer. This method is used with the 'Start' button as a command.
        When active, the method changes the timer_running variable to True, making the Start buttons state='disabled'.
        This was done to avoid overlaping."""
        global REPS
        if self.timer_running:
            return
        self.timer_running = True
        self.start_t_button.config(state="disabled")
        REPS += 1
        if REPS % 8 == 0:
            self.count_down(self.long_brake)
            self.text_label.config(text="Brake", fg=RED)
        elif REPS % 2 == 0:
            self.count_down(self.short_brake)
            self.text_label.config(text="Short Brake", fg=PINK)
        else:
            self.count_down(self.time_left)
            self.text_label.config(text="Work", fg=GREEN)

    def layout(self):
        """Places the layout of the buttons/labels. If you create another label/button, 
        call it trough this function to appear on the main screen."""
        self.canvas_for_image()
        self.timer_text_label()
        self.check_mark_label()
        self.start_button()
        self.reset_button()


if __name__ == "__main__":
    app = Pomodoro()
    app.mainloop()