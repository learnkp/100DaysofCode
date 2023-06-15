from tkinter import *
import random
import ctypes
from Day_85.data import templates
import _tkinter


# -----------------------------ADD FUNCTIONALITY-------------------- #


def stop_test():
    global write_able
    write_able = False

    # get no of words user entered
    no_of_words = len(left_lebel.cget("text").split(" "))

    # Destroy all unwanted widgets.
    remaining_secs_label.destroy()
    current_letter_label.destroy()
    left_lebel.destroy()
    right_label.destroy()
    instruction_label.destroy()
    note_label.destroy()

    # Display the test results with a formatted string
    global result_label
    result_label = Label(text=f'Words per Minute: {no_of_words}', fg='black')
    result_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restart the game
    global result_button
    result_button = Button(text=f'Retry', command=restart)
    result_button.place(relx=0.5, rely=0.6, anchor=CENTER)


def key_press(event=None):
    try:
        if event.char.lower() == right_label.cget('text')[0].lower():
            # Deleting one from the right side.
            right_label.configure(text=right_label.cget('text')[1:])
            # Deleting one from the right side.
            left_lebel.configure(text=left_lebel.cget('text') + event.char.lower())
            # set the next Letter Lavbel
            current_letter_label.configure(text=right_label.cget('text')[0])
    except _tkinter.TclError:
        pass


def add_second():
    # Add a second to the counter.
    global passed_seconds
    passed_seconds += 1
    remaining_secs_label.configure(text=f'{passed_seconds} Seconds')

    # call this function again after one second if the time is not over.
    if write_able:
        window.after(1000, add_second)


def restart():
    # Destry result widgets
    result_label.destroy()
    result_button.destroy()

    # re-setup writing labels.
    rewrite_labels()


# ------------------------------UI SETUP------------------------------ #

# For a sharper window
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# setup a window
window = Tk()
window.title("Typing Speed Test")
window.config(width=700, height=700)

# set default font for the widgets in the window
window.option_add("*Label.Font", "consolas 30")
window.option_add("*Button.Font", "consolas 30")


def rewrite_labels():
    # instruction
    global instruction_label
    instruction_label = Label(text="Instruction: Timer begun start typing now, The typed text converted to grey",
                              font=("arial", 14, "normal"), fg="white", bg="red")
    instruction_label.place(relx=0.05, rely=0.1)

    # timer label is shown below
    global remaining_secs_label
    remaining_secs_label = Label(text=f"0 Seconds", fg="grey")
    remaining_secs_label.place(relx=0.2, rely=0.3)

    # we placed both, one where the written text is and one where the text that will be written, in the same x and
    # y axis so that user doesn't see. and user will see, once user start typing the user text will convert into
    # gery color as mentioned in the left_label code below.
    text = random.choice(templates).lower()
    splitPoint = 0

    global left_lebel
    left_lebel = Label(text=text[0:splitPoint], fg='grey')
    left_lebel.place(relx=0.2, rely=0.5, anchor=E)

    global right_label
    right_label = Label(text=text[splitPoint:])
    right_label.place(relx=0.2, rely=0.5, anchor=W)

    # instruction
    global note_label
    note_label = Label(text="Note:Next letter, which you need to enter shown below", font=("arial", 12, "normal"),
                       bg="red", fg="white")
    note_label.place(relx=0.2, rely=0.6)

    # next letter which user need to enter shown in this label
    global current_letter_label
    current_letter_label = Label(text=text[splitPoint], fg="grey")
    current_letter_label.place(relx=0.2, rely=0.7)
    global write_able
    write_able = True
    window.bind("<Key>", key_press)

    global passed_seconds
    passed_seconds = 0

    # Binding callbacks to functions after a certain amount of time.
    window.after(60000, stop_test)
    window.after(1000, add_second)


# start the test
rewrite_labels()

window.mainloop()
