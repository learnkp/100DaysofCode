from PIL import Image, ImageDraw, ImageFont
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import PIL.Image

img_file = ""


# -----------Add functionality----------------------==#


def add_watermark(input_image, output_image, watermarking_text, xy_pos):
    image = PIL.Image.open(input_image)
    edit_image = ImageDraw.Draw(image)
    fill_color = (20, 108, 148)
    watermark_font = ImageFont.truetype("arial.ttf", 60)
    edit_image.text(xy_pos, watermarking_text, font=watermark_font, fill=fill_color)
    image.show()
    image.save(output_image)


def select_image():
    global img_file
    img_file = askopenfilename()
    if img_file:
        messagebox.showinfo("Image selection",
                            "You have successfully selected your image.")


def watermark_image():
    if img_file == "":
        messagebox.showerror("No image was found", "Please select the image first")
    elif len(watermark_entry.get()) == 0:
        messagebox.showerror("Type your message",
                             "Please enter your text,"
                             " which you wanna watermarked.")
    else:
        img_output = f"profile.png"
        text_watermark = watermark_entry.get()
        add_watermark(img_file, img_output, watermarking_text=text_watermark, xy_pos=(1050, 700))
        messagebox.showinfo("completed",
                            "Successfully watermarked your image!."
                            " Check your logs to see your watermarked photo.")


# ----------------UI SETUP -------------------------#


window = Tk()
window.title("Image Watermark App")
window.config(padx=40, pady=40, bg="#F2BE22")

# label
label = Label(text="Watermark Your \nImage?",
              font=("Courier", 33, "bold"),
              fg="#22A699", bg="#F2BE22")
label.grid(column=0, row=0, columnspan=2)

watermark_text = Label(text="Watermark Text:",
                       font=("arial", 18, "bold"),
                       fg="#22A699", bg="#F2BE22")
watermark_text.config(pady=30)
watermark_text.grid(column=0, row=1)

# buttons
select_img_button = Button(text="Select Image",
                           font=("arial", 16, "normal"),
                           width=35, foreground="#22A699",
                           command=select_image)
select_img_button.grid(column=0, row=2, columnspan=2)

add_watermark_button = Button(text="Add Watermark",
                              font=("arial", 16, "normal"),
                              width=35, foreground="#22A699",
                              command=watermark_image)
add_watermark_button.grid(column=0, row=3, columnspan=2, pady=20)

# entry
watermark_entry = Entry(width=28, relief='solid')
watermark_entry.focus()
watermark_entry.grid(column=1, row=1, ipadx=35, ipady=4)

window.mainloop()

# -------------------------------------------------------------#
