import tkinter as tk
from tkinter import ttk
import winsound

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер")
        self.time = [0, 0, 0]
        self.is_running = False
        self.timer_id = None

        self.hours_var = tk.StringVar(value='00')
        self.minutes_var = tk.StringVar(value='00')
        self.seconds_var = tk.StringVar(value='00')

        self.create_widgets()

    def create_widgets(self):
        self.time_label = tk.Label(self.master, textvariable=self.hours_var)
        self.time_label.grid(row=0, column=0, padx=10, pady=10)

        self.time_label = tk.Label(self.master, text=":")
        self.time_label.grid(row=0, column=1)

        self.time_label = tk.Label(self.master, textvariable=self.minutes_var)
        self.time_label.grid(row=0, column=2, padx=10, pady=10)

        self.time_label = tk.Label(self.master, text=":")
        self.time_label.grid(row=0, column=3)

        self.time_label = tk.Label(self.master, textvariable=self.seconds_var)
        self.time_label.grid(row=0, column=4, padx=10, pady=10)

        self.start_button = tk.Button(self.master, text="Старт", command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(self.master, text="Стоп", command=self.stop_timer)
        self.stop_button.grid(row=1, column=1, padx=10, pady=10)

        self.reset_button = tk.Button(self.master, text="Сбросить", command=self.reset_timer)
        self.reset_button.grid(row=1, column=2, padx=10, pady=10)

        self.hours_combobox = ttk.Combobox(self.master, values=list(range(24)), width=2, state="readonly")
        self.hours_combobox.current(0)
        self.hours_combobox.grid(row=2, column=0, padx=10, pady=10)

        self.minutes_combobox = ttk.Combobox(self.master, values=list(range(60)), width=2, state="readonly")
        self.minutes_combobox.current(0)
        self.minutes_combobox.grid(row=2, column=2, padx=10, pady=10)

        self.seconds_combobox = ttk.Combobox(self.master, values=list(range(60)), width=2, state="readonly")
        self.seconds_combobox.current(0)
        self.seconds_combobox.grid(row=2, column=4, padx=10, pady=10)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            if self.time == [0, 0, 0]:
                self.time = [
                    int(self.hours_combobox.get()),
                    int(self.minutes_combobox.get()),
                    int(self.seconds_combobox.get())
                ]
            self.update_time()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            if self.timer_id:
                self.master.after_cancel(self.timer_id)
                self.timer_id = None

    def reset_timer(self):
        self.stop_timer()
        self.time = [0, 0, 0]
        self.update_display()

    def play_sound(self):
        winsound.Beep(1000, 1000)
    
    def update_time(self):
        if self.time == [0, 0, 0]:
            self.play_sound()
            self.stop_timer()
        else:
            if self.is_running:
                if self.time[2] > 0:
                    self.time[2] -= 1
                elif self.time[1] > 0:
                    self.time[2] = 59
                    self.time[1] -= 1
                elif self.time[0] > 0:
                    self.time[2] = 59
                    self.time[1] = 59
                    self.time[0] -= 1

            self.update_display()
            self.timer_id = self.master.after(1000, self.update_time)

    def update_display(self):
        self.hours_var.set(str(self.time[0]).zfill(2))
        self.minutes_var.set(str(self.time[1]).zfill(2))
        self.seconds_var.set(str(self.time[2]).zfill(2))

root = tk.Tk()
timer = Timer(root)
root.mainloop()