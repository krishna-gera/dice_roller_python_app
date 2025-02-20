import tkinter as tk
from PIL import Image, ImageTk
import random

def rolling_dice():
    dice_image_path = random.choice(dice_images)
    dice_image = ImageTk.PhotoImage(Image.open(dice_image_path))
    image_label.configure(image=dice_image)
    image_label.image = dice_image

root = tk.Tk()
root.geometry('400x400')
root.title("Roll the Dice")

dice_images = [
    r"Python Projects\dice-jpg\dice1.jpg",
    r"Python Projects\dice-jpg\dice2.jpg",
    r"Python Projects\dice-jpg\dice3.jpg",
    r"Python Projects\dice-jpg\dice4.jpg",
    r"Python Projects\dice-jpg\dice5.jpg",
    r"Python Projects\dice-jpg\dice6.jpg"
]

image_label = tk.Label(root)
image_label.pack(expand=True)

roll_button = tk.Button(root, text="Roll the dice", fg="white", bg="black", command=rolling_dice)
roll_button.pack(expand=True)

rolling_dice()

root.mainloop()
