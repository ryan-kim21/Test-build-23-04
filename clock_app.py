import tkinter as tk
import time

class Clock(tk.Label):
    def __init__(self, master=None):
        super().__init__(master)
        self.update_time()

    def update_time(self):
        now = time.strftime('%H:%M:%S')
        self.configure(text=now)
        self.after(1000, self.update_time)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Clock App')
    clock = Clock(root)
    clock.pack()
    root.mainloop()
