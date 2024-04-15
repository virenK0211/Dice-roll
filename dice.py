import tkinter as tk                #this module is used to create GUI (Graphical User Interface)
from PIL import Image, ImageTk      #this module is used to open images and display them on the GUI 
import random                        #this module is used to generate random numbers 
window = tk.Tk()                     #this line creates a window object which is used to create GUI 
window.geometry("500x500")           #this line sets the size of the window (500x500)
window.title("Dice Roll")             #this line sets the title of the window (Dice Roll


#Be carefull when you giving the path of images to the list.
dice = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]  # this line creates a list of images


image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))   # this line opens an image from the list and displays it on the GUI 
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))  # this line opens an image from the list and displays it on the GUI

label1=tk.Label(window, image=image1)     # this line creates a label object and displays the image on the GUI
label2=tk.Label(window, image=image2)     # this line creates a label object and displays the image on the GUI
image_width=100                           # this line sets the width of the image
image_height=100                          # this line sets the height of the image


label1.image = image1                     # this line sets the image on the label object
label1.image = image1                     # this line sets the image on the label object

label1.place(x=0, y=100)                  # this line places the label object on the GUI
label2.place(x=600, y=100)                # this line places the label object on the GUI 
def roll():                               

    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))          # this line opens an image from the list and displays it on the GUI
    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))          # this line opens an image from the list and displays it on the GUI

    label1.configure(image=image1)               # this line sets the image on the label object
    label2.configure(image=image2)               # this line sets the image on the label object

    label1.image = image1                  # this line sets the image on the label object
    label2.image = image2                  # this line sets the image on the label object

button=tk.Button(window, text="ROLL", bg = "blue" , fg="white" , command=roll)  # this line creates a button object and displays it on the GUI
button.place(x=830, y=1)     # this line places the button object on the GUI

window.mainloop()                 # this line starts the GUI event loop and waits for user input

