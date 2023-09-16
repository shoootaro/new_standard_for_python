import tkinter as tk

root = tk.Tk()
root.title("Entryの検証2")
root.geometry("400x100")

def validate_entry(strings):
    if len(strings) < 4:
        add_button["state"] = "disabled"
    else:
        add_button["state"] = "normal"
    return True

strVar = tk.StringVar()

val_cmd = root.register(validate_entry)

entry = tk.Entry(root, width=20, textvariable=strVar,
                 validatecommand=(val_cmd, "%P"),
                 validate="key")
entry.pack()

add_button = tk.Button(root, text="通知", command = lambda:print(strVar.get()))
add_button.pack()
add_button["state"] = "disabled"

root.mainloop()