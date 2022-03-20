import tkinter as ttk
import requests
import threading


class Window(ttk.Frame):
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = ttk.Tk()
app = Window(root)
root.geometry('400x200')


def ee():
    data = {
        'content': content.get()
    }
    if username.get(): data["username"] = username.get()
    if avatar.get(): data["avatar_url"] = username.get()
    x = requests.post(webhook_entry.get(), data=data)
    print(x)


def send():
    threading.Thread(target=ee).start()


ttk.Label(root, text="Webhook URL*", font=('Arial', 14)).grid(row=1, column=1)
webhook_entry = ttk.Entry(root, bd=1, show=None, font=('Arial', 14))
webhook_entry.grid(row=1, column=2)

ttk.Label(root, text="Content*", font=('Arial', 14)).grid(row=2, column=1)
content = ttk.Entry(root, bd=1, show=None, font=('Arial', 14))
content.grid(row=2, column=2)

ttk.Label(root, text="Username", font=('Arial', 14)).grid(row=3, column=1)
username = ttk.Entry(root, bd=1, show=None, font=('Arial', 14))
username.grid(row=3, column=2)

ttk.Label(root, text="Avatar url", font=('Arial', 14)).grid(row=4, column=1)
avatar = ttk.Entry(root, bd=1, show=None, font=('Arial', 14))
avatar.grid(row=4, column=2)

M3 = ttk.Button(root, text="Send", command=send)
M3.grid(row=7, column=2)

# set window title
root.wm_title("Discord webhook")
root.iconbitmap('favicon.ico')

# show window
root.mainloop()
