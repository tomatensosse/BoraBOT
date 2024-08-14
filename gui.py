import tkinter as tk
import threading
import time
import schedule
import trading_bot as bot
from tkinter import PhotoImage


def run_scheduler():
    schedule.every(1).minutes.do(bot.execute_strategy)

    while True:
        schedule.run_pending()
        time.sleep(1)  # Wait a bit before checking the schedule again


def on_start():
    global scheduler_thread
    if scheduler_thread is None or not scheduler_thread.is_alive():
        scheduler_thread = threading.Thread(target=run_scheduler)
        scheduler_thread.start()
        status_label.config(text="Scheduler started.")


def on_stop():
    global running
    running = False


# Initialize the GUI
def start_gui():
    global scheduler_thread
    global running
    global status_label

    root = tk.Tk()
    root.title("Trading Bot")
    root.geometry("400x300")

    try:
        root.iconbitmap('src/app.bmp')
    except Exception as e:
        print(f"Could not set .ico icon: {e}")

    try:
        img = PhotoImage(file='src/app.png')
        root.iconphoto(True, img)
    except Exception as e:
        print(f"Could not set .png or .gif icon: {e}")

    start_button = tk.Button(root, text="Start", command=on_start)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop", command=on_stop)
    stop_button.pack(pady=10)

    status_label = tk.Label(root, text="Scheduler stopped.")
    status_label.pack(pady=10)

    scheduler_thread = None
    running = True

    root.mainloop()
