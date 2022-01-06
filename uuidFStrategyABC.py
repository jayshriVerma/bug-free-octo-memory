import tkinter as tk
import uuid
from abc import ABC, abstractmethod
import string
import random


def generate_uuid1():  #functional version of strategy pattern
    return uuid.uuid1()


def generate_uuid4():
    return uuid.uuid4()


def generate_string_id():
    return "".join(random.choices(string.ascii_lowercase, k=30))


class Model:
    uuid = []


class View(ABC):
    @abstractmethod
    def setup(self, controller):  #setting up UI
        pass

    @abstractmethod
    def append_to_list(self, item):
        pass

    @abstractmethod
    def clear_list(self):
        pass

    @abstractmethod
    def start_main_loop(self):
        pass


class Controller:  #since this is a job of controller to manage this function we hav to add extra parameter generate_uuid
    def __init__(self, model: Model, view: View, generate_uuid):
        self.model = model
        self.view = view
        self.generate_uuid = generate_uuid

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        self.model.uuid.append(self.generate_uuid())
        # now instead of calling function directly call generate_uuid
        self.view.append_to_list(self.model.uuid[-1])

    def handle_click_clear_list(self):
        self.model.uuid = []
        self.view.clear_list()


class TkView(View):  #interspecific implementation of the view
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


c = Controller(
    Model(), TkView(), generate_string_id
)  #now we have to change the function here oly,obviously the power of strategy pattern
#here o change has to made in controller and view ,so MVC we are implemention functional stategy pattern
c.start()
