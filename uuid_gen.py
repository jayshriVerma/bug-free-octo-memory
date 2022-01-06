import tkinter as tk
import uuid


class UUIDGen():
    def __init__(self):
        #setting up the tkinter
        self.root = tk.TK()
        self.root.geometry("500x500")
        self.root.title("UUID_Generation")

        #create the gui
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text="Show")
        self.label.pack()
        self.list = tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH, expand=1)
        self.generate_uuid_button = tk.Button(
            self.frame,
            text="Generate UUID",
            command=self.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button = tk.Button(self.frame,
                                      text="Clear List",
                                      command=self.handle_click_clear_list)
        self.clear_button.pack()

        self.uuid = []
        self.root.mainloop()

    def handle_click_generate_uuid(self):
        self.uuid.append(uuid.uuid4())
        self.list.insert(tk.END, self.uuid[-1])

    def handle_click_clear_list(self):
        self.uuid = []
        self.list.delete(0, tk.END)


u = UUIDGen()
