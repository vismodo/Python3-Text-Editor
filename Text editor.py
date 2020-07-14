#Author: VismayaAtreya(https://github.com/VismayaAtreya)
#Created in: IDLE 3.8.3
#Type: Template
#Link: https://github.com/VismayaAtreya/Python-Text-Editor/Text Editor.py
#Save repository to: Any one folder

import tkinter as tk #Import tkinter for GUI programming
import os #Import the 'os' module to save a text file
try:
    from PIL import ImageTk, Image #Import ImageTk and Image from the Python Imaging Library module
except:
    print("The PIL module can't be found")
from tkinter import filedialog #Import the tkinter filedialog to ask where to save the file.
from tkinter.messagebox import showinfo #Import showinfo from tkinter.messagebox to show any error that may occur
        
def new_file(): #Define the function to create a new file
    welcome.withdraw() #Withdraw the 'Welcome' window
    editor = tk.Tk() #Create a new window with tkinter called 'editor'
    editor.title('Python Text Editor - Template') #Set the title of the 'editor' window
    code_box = tk.Text(editor) #Create a Text widget in the 'editor' window
    code_box.pack() #Show the 'code_box' Text widget in the 'editor' window
    saveas = tk.Button(editor, command = lambda: savefile(str(code_box.get("1.0","end-1c"))), text = 'Save As') #Create a Button widget in the 'editor' window
    saveas.pack(side='bottom') #Show the 'saveas' Button widget in the 'editor' window
    
def savefile(text): #Define the function to save the file
    try:
        print('Extensions:')
        print('.txt: Text file')
        print('.py: Python File')
        print('.xml: XML File Encoding')
        print('.html: Webpage File')
        print('.md: MarkDown')
        text_file = open(input('Save file as(with extension): '), "w")
        text_file.write(text)
        text_file.close()
    except:
        showinfo("Error", "The file you tried to save resulted in an error") #Use showinfo to give an error

welcome = tk.Tk()
welcome.title('Python Text Editor')
img = ImageTk.PhotoImage(Image.open("Greet.jpeg"))
welcome_pic = tk.Label(welcome, image = img)
welcome_pic.pack(side = "top")
newbut = tk.Button(welcome, command=lambda: new_file(),text="Create a new file")
newbut.pack(side = 'bottom')
welcome.mainloop()

