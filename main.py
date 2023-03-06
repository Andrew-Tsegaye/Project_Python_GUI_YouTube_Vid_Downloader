import tkinter 
import customtkinter
from pytube import YouTube 


def start_download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLable.configure(text="")
        video.download()
        finishLable.configure(text="Downloaded!")
    except:
        finishLable.configure(text="Downloaded Error!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage_of_completion = bytes_download / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completion / 100))

# System Settings 
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Font
my_font = customtkinter.CTkFont(family="sans-serif", size=28)

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link", font=my_font)
title.pack(padx=10, pady=40)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, font=customtkinter.CTkFont(family="sans-serif", size=16), textvariable=url_var)
link.pack()

# Finished Downloading
finishLable = customtkinter.CTkLabel(app, text="")
finishLable.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
