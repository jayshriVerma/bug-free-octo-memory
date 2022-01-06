import tkinter as tk
import uuid


class Model:
    uuid = []


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        self.model.uuid.append(uuid.uuid4())
        self.view.append_to_list(self.model.uuid[-1])

    def handle_click_clear_list(self):
        self.model.uuid = []
        self.view.clear_list()


class TkView:
    def setup(self, controller):
        #setting tkinter
        self.root = tk.Tk()
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
            command=controller.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button = tk.Button(
            self.frame,
            text="Clear List",
            command=controller.handle_click_clear_list)
        self.clear_button.pack()

    def append_to_list(self, item):
        self.list.insert(tk.END, item)

    def clear_list(self):
        self.list.delete(0, tk.END)

    def start_main_loop(self):
        self.root.mainloop()


c = Controller(Model(), TkView())
c.start()
