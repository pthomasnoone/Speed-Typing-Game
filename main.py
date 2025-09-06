from tkinter import *
from paragraphs import paragraph_dict
import random

GRAY = "#333333"
DARK_GRAY = "#555555"
timer = None
current_word_list = []
current_index = 0
game_active = False

# Starts the game when button is click by starting the timer and word generator functions
def start_game():
    global game_active
    game_active = True
    start_button.config(state=DISABLED)
    count_down()
    word_generator()

# Submits word when space bar is pressed
def submit_entry(event=None):
    global current_index

    if not game_active:
        return

    typed_word = word_entry.get().strip()
    word_entry.delete(0, END)
    if typed_word == current_word_list[current_index]:
        current_index += 1
        canvas.itemconfig(score_text, text=f"Score: {current_index}")
        word_label.config(text=current_word_list[current_index])

# Countdown timer
def count_down(count=60):
    global game_active
    canvas.itemconfig(timer_text, text=f"{count}s")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        game_active = False
        word_label.config(text="Time's up!")

# Resets the game
def reset_game():
    global current_index
    window.after_cancel(timer)
    current_index = 0
    canvas.itemconfig(timer_text, text="60s")
    word_label.config(text="Type this word.")
    word_entry.delete(0, END)
    canvas.itemconfig(score_text, text=f"Score: {current_index}")
    start_button.config(state=NORMAL)

# Chooses a random list of words and puts the first word on the screen
def word_generator():
    global current_word_list, current_index
    current_word_list = random.choice(list(paragraph_dict.values()))
    word_label.config(text=current_word_list[current_index])


window = Tk()
window.title("Type Speed Test")
window.config(padx=20, pady=20, bg=GRAY)

# Clock Canvas
canvas = Canvas(width=399, height=500, highlightthickness=0)
clock_img = PhotoImage(file="clock.png")
canvas.create_image(199.5, 250, image=clock_img)
timer_text = canvas.create_text(199.5, 250, text="60s", fill="black", font=("Arial", 64, "bold"))
score_text = canvas.create_text(199.5, 175, text=f"Score: {current_index}", fill="black", font=("Arial", 32, "bold"))
canvas.grid(column=1, row=0, pady=20)

# Start Button
start_button = Button(text="Start", command=start_game, bg=DARK_GRAY, fg="white", font=("Arial", 14, "bold"))
start_button.grid(column=0, row=3)

# Reset Button
reset_button = Button(text="Reset", command=reset_game, bg=DARK_GRAY, fg="white", font=("Arial", 14, "bold"))
reset_button.grid(column=2, row=3)

# Word Label
word_label = Label(text="Type this word.", font=("Arial", 24, "bold"), fg="white", bg=GRAY)
word_label.grid(column=1, row=1, pady=10)

# Word Entry
word_entry = Entry(width=15, font=("Arial", 24, "bold"), highlightthickness=0)
word_entry.grid(column=1, row=2, pady=10)
word_entry.focus()
word_entry.bind('<space>', submit_entry)



window.mainloop()



