import tkinter as tk
from tkinter import messagebox

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return 1.5 * 1.732 * self.side_length**2

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 6 * 120

    def display(self):
        result_text.set(
            f"Hexagon:\n"
            f"Area: {self.calcArea():.2f}\n"
            f"Perimeter: {self.calcPeri()}\n"
            f"Sum of angles: {self.calcAngleSum()}"
        )


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length**2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def display(self):
        result_text.set(
            f"Square:\n"
            f"Area: {self.calcAreaSquare():.2f}\n"
            f"Perimeter: {self.calcPeriSquare()}"
        )


def on_hexagon_button():
    hexagon = Hexagon(9)
    hexagon.display()


def on_square_button():
    square = Square(10)
    square.display()


def on_exit_button():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()


root = tk.Tk()
root.title("Geometry Calculator")
root.geometry("400x400")

result_text = tk.StringVar()

hexagon_button_label = tk.Label(root, text="Hexagon")
hexagon_button_label.pack(pady=1)
hexagon_button = tk.Button(root, text="        1        ", command=on_hexagon_button)
hexagon_button.pack(pady=1)

square_button_label = tk.Label(root, text="Square")
square_button_label.pack(pady=1)
square_button = tk.Button(root, text="        2        ", command=on_square_button)
square_button.pack(pady=1)

exit_button = tk.Button(root, text="     Exit     ", command=on_exit_button)
exit_button.pack(pady=10)

result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT, font=("Courier", 12), bd=2, relief=tk.SUNKEN)
result_label.pack(pady=10, expand=True, fill=tk.BOTH)

root.mainloop()
