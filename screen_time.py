import tkinter as tk
import time
import argparse

def show_message():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background='black')
    label = tk.Label(root, text="Time for a break?", font=("Helvetica", 48), fg="white", bg="black")
    label.pack(expand=True)
    root.update()
    for i in range(5, 0, -1):
        label.config(text=f"Time for a break? {i}")
        root.update()
        time.sleep(1)
    root.destroy()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set the number of minutes to wait between screen flashes.")
    parser.add_argument("minutes", type=int, nargs='?', default=60,
        help="Number of minutes to wait between screen flashes (default: 60)")
    args = parser.parse_args()

    while True:
        show_message()
        time.sleep(args.minutes * 60)  # Wait for the specified number of minutes