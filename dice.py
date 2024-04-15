import tkinter as tk
from PIL import Image, ImageTk
import random
window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")
# def roll_dice():
#     a=random.randint(1,6)
#     label = tk.Label(window, text=a).pack()


# button = tk.Button(window, text="Roll Dice", command=roll_dice).pack()
# button.pack()


dice=[]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))   
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window, image=image1)
label2=tk.Label(window, image=image2)

label1.image = image1
label1.image = image1

label1.place(x=0, y=100)


window.mainloop()