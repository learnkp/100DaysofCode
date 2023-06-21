from tkinter import *

written_text = ""
counter = 0


# ---------------------------ADD FUNCTIONALITY------------#


def writing_text():
    global written_text, counter
    if len(text_area.get("1.0", END)) > 1 and written_text == text_area.get("1.0", END):
        tagline_label.config(text=f"Deleting in {counter}")
        if counter == 0:
            text_area.delete("1.0", END)
            tagline_label.config(text=f"Start again...")
            window.after(1000, writing_text)
        else:
            window.after(1000, writing_text)
            counter -= 1
    else:
        if len(text_area.get("1.0", END)) > len(written_text) and len(text_area.get("1.0", END)) != 1:
            tagline_label.config(text=f"Continue Typing..")
        written_text = text_area.get("1.0", END)
        counter = 5
        window.after(1000, writing_text)


def save_text():
    with open("data.txt", "a") as file:
        if len(text_area.get("1.0", END)) > 1:
            file.write(text_area.get("1.0", END))
            text_area.delete("1.0", END)
            writing_text()


def clear_text():
    text_area.delete("1.0", END)
    writing_text()


# ---------------------------UI SETUP---------------------#
# create a window

window = Tk()
window.title("Disappearing Text Writing App")
window.config(width=700, height=500, bg="#8EAC50", pady=30, padx=30)

# create your widgets
heading_label = Label(text="Write Your Thoughts Here",
                      font=("arial", 25, "bold"),
                      bg="#8EAC50", fg="#17594A", pady=30, padx=30)
heading_label.grid(column=0, row=0, columnspan=2)

tagline_label = Label(text="Start Typing..", font=("arial", 25, "bold"),
                      bg="#8EAC50", fg="#17594A", )
tagline_label.grid(column=0, row=1, columnspan=2, pady=10)

text_area = Text(width=40, height=8, font=("arial", 14, "bold"),
                 fg="#17594A", )
text_area.focus()
text_area.grid(column=0, row=2, columnspan=2)

clear_button = Button(text="Clear Text", font=("arial", 16, "bold"),
                      bg="#8EAC50", fg="#17594A", command=clear_text)
clear_button.grid(column=0, row=3)

save_button = Button(text="Save", font=("arial", 16, "bold"),
                     bg="#8EAC50", fg="#17594A", width=10,
                     command=save_text)
save_button.grid(column=1, row=3, pady=20, )

instruction_label = Label(text="NOTE: If you stop writing more then 5 seconds,"
                               " \nthe written text will be disappear.",
                          bg="#8EAC50", fg="red", font=("arial", 16, "bold"))
instruction_label.grid(column=0, row=4, columnspan=2, )

writing_text()
window.mainloop()
