from google import genai
import os
import tkinter

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat=client.chats.create(model="gemini-2.5-flash")

file = client.files.upload(file="FIT 2107 Reflection - Jijendran.pdf")

res = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=["Summarise what is needed of me from this document",file]
)

tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief="ridge", borderwidth=2)
frame.pack(fill = "both", expand=1)
label = tkinter.Label(frame, text=res.text) # type: ignore
label.pack(fill = "x", expand=1)

tk.mainloop()


"""
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
"""