import tkinter as tk
from tkinter import messagebox

def send_alert():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the alert pop-up
    messagebox.showinfo("Human Detected Alert", "A human has been detected in the image!")

    # Close the window after showing the message
    root.quit()

if __name__ == "__main__":
    send_alert()
