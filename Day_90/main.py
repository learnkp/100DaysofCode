import os
import PyPDF2
from gtts import gTTS
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

text = ""


# -------------------ADD FUNCTIONALITY---------------#


def open_pdf():
    """This function takes a pdf file from local system. Convert pdf file
    into number of pages, respective to pdf.
     And data within that page converted to text as output"""
    global text
    file_location = askopenfilename()
    if file_location:
        with open(file_location, "rb") as file:
            pdf = PyPDF2.PdfReader(file)
            for num_page in range(len(pdf.pages)):
                page_obj = pdf.pages[num_page]
                text += page_obj.extract_text()
        messagebox.showinfo("Select PDF File", "You have successfully selected "
                                               "the pdf file")
    else:
        messagebox.showerror("Select PDF File", "You haven't selected any pdf file")


def play_audio():
    """This function generates a audiofile of given text"""
    messagebox.showinfo("Convert PDF to Audiobook",
                        "Wait a moment, it will take sometime to convert to mp3")
    global text
    final_output = gTTS(text=text, lang="en")
    print("generating speech")
    final_output.save("Day_90/output.mp3")
    os.system("start Day_90/output.mp3")


# --------------------------UI SETUP---------------------- #

# initialize window
window = Tk()
window.title("PDF to Audiobook")
window.config(padx=40, pady=40, bg="#E7CEA6")

# create widgets
title_label = Label(text="Convert PDF to Audiobook",
                    font=("arial", 40, "bold"),
                    fg="#0A6EBD",
                    bg="#E7CEA6")
title_label.grid(column=0, row=0, pady=40, columnspan=2)

open_pdf_btn = Button(text="Select PDF",
                      font=("courier", 25, "bold"), width=15,
                      fg="#0A6EBD", bg="#E7CEA6",
                      command=open_pdf)
open_pdf_btn.grid(column=0, row=2, pady=5)

play_audio_btn = Button(text="Play Audio", font=("courier", 25, "bold"),
                        width=15, fg="#0A6EBD", bg="#E7CEA6",
                        command=play_audio)
play_audio_btn.grid(column=1, row=2, padx=20)


window.mainloop()

# --------------------------------------------------------------------#
