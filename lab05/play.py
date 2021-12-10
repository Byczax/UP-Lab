# import required libraries
from pydub import AudioSegment
from pydub.playback import play
import sys
import tkinter as tk
from tkinter.constants import HORIZONTAL
from tkinter import filedialog
from playsound import playsound
import threading
import os

root = tk.Tk()  # declaration where is gui ?maybe?

filename = ""

class app(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # self.master = master
        # self.pack()
        root.geometry("700x300")  # setting the gui size
        self.create_widgets()
        

    def create_widgets(self):
        def exit():
            print("lol")
            os._exit(0)
            # sys.exit(0)
            

        def browse_files():
            global filename
            filename = filedialog.askopenfilename(title="Select a File", filetypes=(
                ("Audio files", ["*.wav", "*.mp3"]), ("all files", "*.*")))
            label_file_explorer.configure(
                text="File Selected: "+filename.split("/")[-1])

        def play_selected_file():
            global filename
            global play_thread
            # print(filename)
            # print(filename.split("/")[-1].split(".")[-1])
            # audio_file = AudioSegment.from_file(file = filename,format = filename.split("/")[-1].split(".")[-1])
            # play_selected_file.t
            play_thread = threading.Thread(target=playsound, args=(filename,))
            play_thread.start()
            
            # root.destroy()
            # play(audio_file)

        label_file_explorer = tk.Label(root,
                                       text="File Explorer using Tkinter",
                                       width=100, height=4,
                                       fg="blue")

        # self.label = tk.Label(
        #     self, text="Hello there, general kenobi, select your desired options")
        # self.label.pack()
        hello_label = tk.Label(
            root, text="Hello there, general kenobi, select your desired file", height=2)

        button_explore = tk.Button(root,
                                   text="Browse Files",
                                   command=browse_files)
        button_play = tk.Button(root, text="Play file", command=play_selected_file, fg="Green")
        button_exit = tk.Button(root, text="Exit", command=exit, fg="Red")

        hello_label.grid(column=1, row=1)
        button_explore.grid(column=1, row=2)
        label_file_explorer.grid(column=1, row=3)
        button_play.grid(column=1, row=4)
        button_exit.grid(column=1, row=6)

        # label_file_explorer.grid(column = 1, row = 1)
        # selected_drawing_type = tk.StringVar()
        # selected_drawing_type.set("Dots")  # set default value
        # self.option_menu = tk.OptionMenu(
        #     self, selected_drawing_type, "Dots", "Lines", "Triangles", "Triangle strips")
        # self.option_menu.pack()

        # selected_render = tk.StringVar()
        # selected_render.set("Egg")
        # self.render_menu = tk.OptionMenu(
        #     self, selected_render, "Egg", "Torus")
        # self.render_menu.pack()

        # self.detail_slider = tk.Scale(
        #     self, from_=1, to=50, label="details?", orient=HORIZONTAL)
        # self.detail_slider.set(15)
        # self.detail_slider.pack()

        # self.rotation_speed = tk.Scale(
        #     self, from_=0, to=100, label="how faaaaaast?", orient=HORIZONTAL)
        # self.rotation_speed.set(20)
        # self.rotation_speed.pack()
        # buttons
        # self.button = tk.Button(
        #     self, text="Accept selected values", command=when_click, fg="Green")
        # self.button.pack()
        # self.button = tk.Button(
        #     self, text="Exit", command=exit, fg="Red")
        # self.button.pack()

# Import an audio file
# Format parameter only
# for readability


def main():
    app(master=root).mainloop()

    
# Play the audio file
    # play(audio_file)


if __name__ == "__main__":
    main()
