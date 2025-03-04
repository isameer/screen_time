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
    assert args.minutes >= 1

    while True:
        for time_left in range(args.minutes, 0, -1):
            print(f"Time left: {time_left} minutes")
            time.sleep(1 * 60)
        show_message()
        