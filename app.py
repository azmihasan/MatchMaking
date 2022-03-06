import tkinter as tk
from tkinter import Text
import os

root = tk.Tk()

# # base or primary layer
# canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# canvas.pack()
# # frame or secondary layer
# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
# 10 participants, each has own label



#input
entry = tk.Entry(width=5)
entry.pack()

inputParticipant = tk.Button(root, text="Input Participant", padx=10, 
                     pady=5, fg="white", bg="#263D42")
inputParticipant.pack()

match = tk.Button(root, text="Match", padx=10, 
                     pady=5, fg="white", bg="#263D42")

match.pack()

root.mainloop()